import sublime, sublime_plugin, os, source_tools

class Actionscript3Import(sublime_plugin.TextCommand):
	def run(self, edit):
		# Get the word we'll search for
		current_word_region = self.view.word(self.view.sel()[0])
		current_word = self.view.substr(current_word_region)

		# insert the instruction
		# self.view.insert(edit, 0, SourceTools.project_path(self.view.file_name()))
