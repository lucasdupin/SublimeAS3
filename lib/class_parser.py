class ClassParser(object):
	""" """
	def __init__(self, view):
		self.view = view

		self.properties = []
		self.gettersetters = []
		self.methods = []
		self.static_properties = []
		self.static_methods = []
		