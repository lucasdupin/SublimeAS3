import sublime, sublime_plugin, sys
sys.path.append('lib')
from class_parser import ClassParser

class AS3Autocomplete(sublime_plugin.EventListener):
	"""Autocomplete for AS3"""
	
	def on_query_completions(self, view, prefix, locations):
		
		cp = ClassParser(view)
		comp_list = []

		comp_list += cp.properties
		comp_list += cp.gettersetters
		comp_list += cp.methods
		comp_list += cp.static_properties
		comp_list += cp.static_methods

		return [(x, x) for x in comp_list]