import sublime, sublime_plugin, os, sys
sys.path.append('lib')
import source_tools

class Actionscript3Debug(sublime_plugin.TextCommand):
	"""
	Open project
	"""
	def run(self, edit):
		print os.path.join(sublime.packages_path(), 'ActionScript3', 'bin', 'as3Debugger.app')
		os.system("open %s" % (os.path.join(sublime.packages_path(), 'ActionScript3', 'bin', 'as3Debugger.app').replace(' ','\ ')))
