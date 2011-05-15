import sublime, sublime_plugin, source_tools

class AS3Autocomplete(sublime_plugin.EventListener):
	"""Autocomplete for AS3"""
	
	def on_query_completions(self, view, prefix, locations):
		return ["alo"];