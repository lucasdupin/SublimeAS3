import os, yaml, build_validator, swc_dump, re, sys
from os.path import *

class SourceTools(object):
	"""Project related stuff"""
	def __init__(self, file_name, st_lib_path=None):
		self.file_name = file_name
		self.project_path = self.get_project_path()
		self.config = self.load_config()
		self.st_lib_path = st_lib_path # Don't know why but sublime makes my script lose it's path
		# Making sure our build file is valid
		# build_validator.validate(config)
		
	def find_package(self, word):
		""" find import for class """
		# Check if there was no input
		if word == '': return []
		# Search
		return self.search_all_paths(word)

	def get_project_path(self):
		""" 
		Finds build.yaml related to the file_name received
		"""
		path = dirname(self.file_name)
		while path != '/' :
			# Check for build.yaml
			for f in os.listdir(path):
				if f.lower() == "build.yaml":
					return path
			path = dirname(path)
		# Not found
		raise Exception("Could not find build.yaml")

	def load_config(self):
		""" Loads build.yaml """
		yaml_path = join(self.project_path, "build.yaml")
		return yaml.load(file(yaml_path, 'r'))

	def search_all_paths(self, word):
		# Search
		pp = self.search_project_paths(word)
		bp = self.search_bundle_paths(word)
		# Create result array with the correct order
		ordered_paths = pp['exact'] + bp['exact'] + pp['partial'] + bp['partial']
		# removing duplicates (fast way)
		seen = {} 
		result = []
		for item in ordered_paths: 
			if item in seen: continue 
			seen[item] = 1 
			result.append(item) 
		# All done
		return result

	def search_project_paths(self, word):
		swcs = swc_dump.SWCDump(self.project_path, self.config['library-path']);
		source_paths = [join(self.project_path, p) for p in self.config['source-path']]
		# Regexes
		partial_re = re.compile('\\b%s\w*\.(as|mxml)$' % word, re.IGNORECASE)
		exact_re = re.compile('\\b%s$' % word, re.IGNORECASE)
		extension_re = re.compile('\\.(as|mxml)$')
		# Return values
		partial_matches = []; exact_matches = []
		# Search in all paths
		found_paths = []
		for path in source_paths + swcs.dump_paths:
			# all files
			for w in os.walk(path, followlinks=True):
				# check for matches
				for f in w[2]:
					if not partial_re.match(f): continue
					# Found something! Check if it's exact or partial...
					package_name = re.sub(extension_re, '', join(w[0], f).replace(path+'/', '').replace('/','.'))
					if exact_re.match(f):
						exact_matches.append(package_name)
					else:
						partial_matches.append(package_name)
		return {'partial':partial_matches, 'exact':exact_matches}

	def search_bundle_paths(self, word):
		# Return values
		partial_matches = []; exact_matches = []
		partial_re = re.compile("href='([a-zA-Z0-9\\/]*\\b%s\\w*)\\.html'|([a-zA-Z0-9\\/]*\\/package\\.html#%s\\w*)\\(\\)'" % (word, word), re.IGNORECASE)
		exact_re = re.compile('(^|\\.)%s$' % word, re.IGNORECASE)

		# Open document with definitions
		doc = open(join(self.st_lib_path, dirname(__file__), '..', 'data', 'doc_dictionary.xml'))
		# Check for each one
		for line in doc:
			p = partial_re.search(line)
			if p:
				package_name = p.group(1) if p.group(2) is None else p.group(2)
				package_name = package_name.replace('/','.')
				if exact_re.search(package_name):
					exact_matches.append(package_name)
				else:
					partial_matches.append(package_name)
		return {'partial':partial_matches, 'exact':exact_matches}

# Testing
if __name__ == "__main__":
	s = SourceTools("/Users/lucas/src/unimedii/frontend/trunk/source/classes/unimedii_loader.as")
	print s.find_package("Load")