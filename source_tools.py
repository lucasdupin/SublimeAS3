import os, yaml

class SourceTools(object):
	"""Project related stuff"""
	def __init__(self, file_name):
		self.file_name = file_name
		self.project_path = self.get_project_path()
		self.config = self.load_config();
		
	def src_dirs(self):
		pass

	def search_all_paths(self):
		pass

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
		yaml_path = os.path.join(project_path(self.file_name), "build.yaml")
		return yaml.load(file(yaml_path, 'r'))

	
	# def self.common_src_dirs
 #    src_dirs_matches = []
 #    AS3Project.source_path_list.each do |source_path|
 #      source_path.gsub("/",".")
 #      src_dirs_matches << source_path
 #    end
 #    src_dirs_matches << common_src_dir_list.split(":")
 #    src_dirs_matches
 #  end
		