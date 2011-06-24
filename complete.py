import sublime, sublime_plugin, sys
sys.path.append('lib')
import source_tools

class Actionscript3Complete(sublime_plugin.EventListener):
	"""Autocomplete for AS3"""
	
	def on_query_completions(self, view, prefix, locations):
		return ["alo"];