# -*- encoding: utf-8 -*-

import socket

class browser:

	def __init__(self):
		#iniciamos variables
		self.url = ""
		self.contenido = ""
		self.estado = 000
		print("[Browser] creacion")

	def corregirUrl(self, url):
		#vamos a corregir las url y obtener los datos necesarios
		print("[Browser] CorregirUrl")
		pass

	def hacerPeticion(self, host, path, parametros):
		#vamos a hacer la peticion y a devolver el valor obtenido
		print("[Browser] HacerPeticion")
		pass

	def actuar(self, usuario, comando, mensaje):
		#tenemos que devolver un mensaje, no más
		if(comando == 'go' or comando == 'ir'):
			so = socket.socket()
			so.connect((mensaje, 80))
			so.send('''GET / HTTP/1.0
				Host: {0}

				'''.format(mensaje))

			return so.recv(512)