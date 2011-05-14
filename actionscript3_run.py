import sublime, sublime_plugin, source_tools, os

class Actionscript3Run(sublime_plugin.TextCommand):
	"""
	Open project
	"""
	def run(self, edit):
		config = source_tools.config(self.view.file_name())
		project_path = source_tools.project_path(self.view.file_name())
		os.system("open %s" % os.path.join(project_path, config['default'][0]['open']).replace(' ','\ '))
