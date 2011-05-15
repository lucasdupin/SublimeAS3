def validate(config):
	if check_for_key(config, 'default'):
		check_if_is_array(config, 'default')
		if len(config['default']) == 0:
			raise Exception("Default must have at least one item")
		check_for_key(config['default'][0], 'debug')
		check_for_key(config['default'][0], 'open')
		check_for_key(config['default'][0], 'extras')
	if check_for_key(config, 'source-path'):
		check_if_is_array(config, 'source-path')
	if check_for_key(config, 'library-path'):
		check_if_is_array(config, 'library-path')
	if check_for_key(config, 'applications'):
		check_if_is_array(config, 'applications')
		for app in config['applications']:
			check_for_key(app, 'class', "Could not find '%s' inside an application in build.yaml")
			check_for_key(app, 'output', "Could not find '%s' inside an application in build.yaml")
	

def check_for_key(config, key, msg=None):
	if msg is None: msg = "Could not find '%s' in build.yaml"
	if not config.has_key(key):
		raise Exception(msg % key)

def check_if_is_array(config, key):
	if not isinstance(config[key], list): 
		raise Exception("'%s' must be an array" % config)