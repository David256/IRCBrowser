# -*- encoding: utf-8 -*-

import socket
import re

class irc:

	visa = socket.socket()
	nombre = ""
	servidor = ""
	conectado = False


	def __init__(self, nom, realname, serv):
		self.nombre = nom
		self.servidor = serv
		self.realname = realname
		#iniciamos las variables necesarias
		print("[IRC] Creacion")

	def conectar(self):
		print("Conectandose..")
		self.visa.connect((self.servidor, 6667))
		print("Enviando credenciales")
		self.enviar("NICK " + self.nombre)
		self.enviar("USER " + self.nombre + " Usuario Usuario " + self.realname)
		self.conectado = True
		#conectamos y fijamos estados

	def recibir(self):
		recibido = self.visa.recv(512)
		self.enviarPing(recibido)
		return recibido
		#manejamos mensajes que llegan

	def mensaje(self, usuario, mensaje):
		self.enviar('PRIVMSG ' + usuario + ' :' + mensaje)
		#enviamos los datos al usuario que hizo el evento

	def enviar(self, texto):
		self.visa.send(texto + "\n")
		#enviamos datos crudos

	def enviarPing(self, texto):
		if(texto.find('PING')!=-1):
			parte = texto.split(" ")
			if(parte[0] == "PING"):
				print(parte[1][1:])
				self.enviar("PONG " + parte[1][1:])
				print("Se hace PING/PONG")
		#manejamos evento ping/pong

	def informacion(texto):
		# ^(:)(.+)(!)(~?)(.+)(\/)(.+)(\s)(PRIVMSG)(\s)(\w+)(\s)(:)(.*)$
		expresion = '^(:)(.+)(!)(~?)(.+)(\/)(.+)(\s)(PRIVMSG)(\s)(\w+)(\s)(:)(.*)$'
		partes = re.match(expresion, texto)
		usuario = partes[1]
		comando = partes[8]
		destino = partes[10]
		mensaje = partes[13]
		if(comando == 'PRIVMSG' and destino == self.nombre):
			informe = {usuario, mensaje}
			return informe
		else:
			return None