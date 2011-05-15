import os, hashlib, errno, re, shutil, zipfile
from stat import *

class SWCDump(object):

	"""Dumps swcs into temp path so the package will be able to parse them"""
	def __init__(self, project_path, library_paths):
		self.library_paths = library_paths
		self.project_path = project_path
		self.dump_paths = []
		# do the nasty work
		self.dump()

	def dump(self):
		# recreating dump paths
		self.dump_paths = []
		dump_path = self.tmp_swc_dir()
		# Dump from all folders
		for p in self.library_paths:
			# Dump from where to where?
			path_from = os.path.join(self.project_path, p);
			path_to = os.path.join(dump_path, p);
			# Making sure this directory exists
			try:
				os.makedirs(path_to)
			except OSError as e:
				if e.errno == errno.EEXIST: pass
			# Dumping each swc
			is_swc = re.compile('\.swc$')
			for swc in os.listdir(os.path.join(self.project_path, p)):
				# Only swcs
				if not is_swc.search(swc): continue

				# Paths
				swc_path_to = os.path.join(path_to, swc)
				swc_path_from = os.path.join(path_from, swc)
				self.dump_paths.append(swc_path_to + "/classes")

				# Check if the swc is older than the extraction
				# We don't want to waste our precious CPU loops
				should_dump = not os.path.isdir(swc_path_to) or os.stat(swc_path_from)[ST_MTIME] > os.stat(swc_path_to)[ST_MTIME]

				if should_dump:
					# removing old files
					shutil.rmtree(swc_path_to, True)
					class_path = "%s:%s" % (os.path.join(os.path.dirname(__file__), '..', 'bin', 'java'), os.path.join(os.path.dirname(__file__), '..', 'bin', 'java', 'swfutils.jar'))
					class_path = class_path.replace(' ', '\ ')
					# unzip swc
					zipfile.ZipFile(swc_path_from).extractall(swc_path_to)
					# run external utility
					result = os.system("java -cp %s Main %s/library.swf %s/classes" % (class_path, swc_path_to, swc_path_to))


	
	def tmp_swc_dir(self):
		project_checksum = hashlib.md5(self.project_path).hexdigest()
		return os.path.join("/tmp/fcshd/swcs/", project_checksum)

# Testing
if __name__ == "__main__":
	s = SWCDump("/Users/lucas/src/unimedii/frontend/trunk", ['source/swc'])
	print s.dump_paths