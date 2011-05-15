import sublime, sublime_plugin, os, sys
sys.path.append('lib')
import source_tools

class Actionscript3Import(sublime_plugin.TextCommand):
	def run(self, edit):
		# Project reference
		st = source_tools.SourceTools(self.view.file_name())

		# Get the word we'll search for
		current_word_region = self.view.word(self.view.sel()[0])
		current_word = self.view.substr(current_word_region)

		matches = st.find_package(current_word.strip())

		if len(matches) == 0:
			sublime.status_message("No package found");
		elif len(matches) == 1:
			# Found only one, let's insert it
			pass
		else:
			# Lots of choices
			pass

		# insert the instruction
		self.view.insert(edit, 0, ','.join(matches))
