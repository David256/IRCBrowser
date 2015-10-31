

class setter:

	def __init__(self):
		#aquí debemos cargar config.json
		self.nombre = "Browser"
		self.realname = "IRCBrowser"
		self.servidor = "irc.hira.io"

	def getNombre(self):
		return self.nombre

	def getRealname(self):
		return self.realname

	def getServidor(self):
		return self.servidor