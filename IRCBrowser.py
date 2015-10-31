# -*- encoding: utf-8 -*-

#
# IRCBrowser:
#
# Creado por David256 para la comunidad HIRA y/o IRC, pero por el momento
# se esta desarrollando. Hey otro-usuario, puedes aprender con mi código
# sin problema, es libre, pero.. no es ético decir que es tuyo cuando no
# lo es.
# Da los respectivos crédito y se felíz. Que tengas un buen <3  día  <3
#
# https://github.com/David256


import sys

import omg.IRC as IRC
import omg.Browser as Browser
import omg.Setter as Setter

#creacion de objetos necesarios
setter = Setter.setter()

irc = IRC.irc( setter.getNombre , setter.getRealname , setter.getServidor )
#objeto del navegador
browser = Browser.browser()


def accion():
	print("[BOT] Loop")
	#aqui los metodo de recivir datos

try:
	#metodo
	irc.conectar()

	while(True):
		accion()
	#fin
	
except Exception as e:
	print("Error Fatal: El bot ha lanzado un error no manejable anteriormente >:( ")
	print("Mas informacion: " + str(e))