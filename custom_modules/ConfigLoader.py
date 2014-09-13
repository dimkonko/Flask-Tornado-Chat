import ConfigParser

class ConfigLoader(object):
	def __init__(self, path):
		self.conf_parser = ConfigParser.ConfigParser()
		self.conf_parser.read(path)

	def load(self):
		section = self.conf_parser.sections()[0]
		options = self.conf_parser.options(section)
		config = dict()
		for option in options:
			config[option] = self.conf_parser.get(section, option)
		return config