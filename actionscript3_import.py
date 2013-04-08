import sublime, sublime_plugin, os, sys, re
sys.path.append('lib')
import source_tools

class Actionscript3Import(sublime_plugin.TextCommand):
	def run(self, edit):
		# Project reference
		st = source_tools.SourceTools(self.view.file_name(), os.path.join(sublime.packages_path(), 'ActionScript3'))

		# Get the word we'll search for
		current_word_region = self.view.word(self.view.sel()[0])
		current_word = self.view.substr(current_word_region)

		matches = st.find_package(current_word.strip())
		
		def on_choose_class(index):
				
				# Nothing selected
				if index == -1:
					return
				
				# Class name
				imp = matches[index];

				cla = imp.split('.').pop()
				# Replace Class name
				self.view.replace(edit, current_word_region, cla)

				# Exit if already imported
				if self.view.find("^\\s*import\\s+%s(\\s|;)" % imp.replace('.', '\\.'), 0):
					return
				# Searching where to add
				pkg = self.view.find("^\\s*package\\b\\s*([\\w+\\.]*)[\\s\\n]*\\{", 0)

				# Calculate
				insert_after = sublime.Region(0, 0) if pkg is None else pkg # after the package, if it exists

				l = self.view.line(insert_after.end())
				self.view.replace(edit, l, "%s\n\timport %s;" % (self.view.substr(l), imp));

				self.view.show(self.view.sel()[0])

		if len(matches) == 0:
			sublime.status_message("No package found");
		elif len(matches) == 1:
			# Found only one, let's insert it
			on_choose_class(0);
		else:
			# Lots of choices
			sublime.active_window().show_quick_panel(matches, on_choose_class);
