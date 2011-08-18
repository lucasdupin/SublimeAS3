import sublime, sublime_plugin, os, sys, re
sys.path.append('lib')
import source_tools

class Actionscript3OrganizeImport(sublime_plugin.TextCommand):

	def run(self, edit):

		# finding all imports
		regions = self.view.find_all( "^\\s+import\\s+.*\.(\\w+?);" )
		imports = []

		# get import string
		for reg in regions:
			class_name = self.view.substr( reg ).split(".").pop().rstrip(";")
			times_used = 0

			# "special" check for i18n (potato.modules.i18n._;) function
			if class_name == "_":
				class_name += "\("
				times_used = 1
			

			times_used += len(self.view.find_all( r'[^\w]%s[^\w]' % class_name ))

			if times_used > 1:
				imports.append( self.view.substr( reg ) )

		# sort and organize line by line
		imports = sorted( imports )
		imports = "\n".join(imports)

		# remove all imports
		while True:
			imp = self.view.find("^\\s+import\\s+.*\.(\w+?);", 0)
			if imp == None:
				break
			else:
				self.view.replace(edit, imp, "")
				insert_reg = imp;
		
		pkg = self.view.find("^\\s*package\\b\\s*([\\w+\\.]*)[\\s\\n]*\\{\\s\\s+?", 0)
		insert_after = sublime.Region(0, 0) if pkg is None else pkg
		
		l = self.view.line( insert_after.end() )

		self.view.replace(edit, l, imports)
