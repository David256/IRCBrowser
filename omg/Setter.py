# -*- encoding: utf-8 -*-

class setter:

	def __init__(self):
		self.nombre = "Browser"
		self.realname = "IRCBrowser"
		self.servidor = "irc.hira.io"
		#aquí debemos cargar config.json

	def getNombre(self):
		return self.nombre

	def getRealname(self):
		return self.realname

	def getServidor(self):
		return self.servidor