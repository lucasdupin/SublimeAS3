import os, yaml


def src_dirs():
	pass

def search_all_paths(self):
	pass

def project_path(file_name):
	path = os.path.dirname(file_name)
	while path != '/' :
		# Check for build.yaml
		for f in os.listdir(path):
			if f.lower() == "build.yaml":
				return path
		path = os.path.dirname(path)
	# Not found
	raise Exception("Could not find build.yaml")

def config(file_name):
	yaml_path = os.path.join(project_path(file_name), "build.yaml")
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
		