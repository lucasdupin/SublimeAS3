import os, yaml, build_validator, swc_dump

class SourceTools(object):
	"""Project related stuff"""
	def __init__(self, file_name):
		self.file_name = file_name
		self.project_path = self.get_project_path()
		self.config = self.load_config()
		# Making sure our build file is valid
		# build_validator.validate(config)
		
	def find_package(self, word):
		""" find import for class """
		# Check if there was no input
		if word == '':
			return []
		
		# Search
		return self.search_all_paths(word)

	def get_project_path(self):
		""" 
		Finds build.yaml related to the file_name received
		"""
		path = os.path.dirname(self.file_name)
		while path != '/' :
			# Check for build.yaml
			for f in os.listdir(path):
				if f.lower() == "build.yaml":
					return path
			path = os.path.dirname(path)
		# Not found
		raise Exception("Could not find build.yaml")

	def load_config(self):
		""" Loads build.yaml """
		yaml_path = os.path.join(self.project_path, "build.yaml")
		return yaml.load(file(yaml_path, 'r'))

	def search_all_paths(self, word):
		# Search
		pp = self.search_project_paths(word)
		bp = self.search_bundle_paths(word)
		# Create result array with the correct order
		ordered_paths = pp['exact'] + bp['exact'] + pp['partial'] + bp['partial']
		# removing duplicates (fast)
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
		for path in self.config['source-path'] + swcs.dump_paths:
			pass
		return {'partial':[], 'exact':[]}
	def search_bundle_paths(self, word):
		return {'partial':[], 'exact':[]}

		