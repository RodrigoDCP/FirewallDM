import itertools
import random
from datetime import datetime, timedelta
import sys
import os
from colorama import init
from termcolor import colored
import time

init()

print(colored("Cargando...", 'yellow'))
time.sleep(1)
os.system('clear')

print(colored('''
 _____          ____        __  __ 
|  ___|_      _|  _ \      |  \/  |
| |_  \ \ /\ / / | | |_____| |\/| |
|  _|  \ V  V /| |_| |_____| |  | |
|_|     \_/\_/ |____/      |_|  |_|
''', 'green'))
print(colored("		By Cañas", 'yellow'))
print(colored("			version - 1.2", 'yellow'))


# [1] -----------------------------------------------

def status():
	print(colored("Verificando estado del Firewall...", 'yellow'))
	time.sleep(1)
	os.system('firewall-cmd --state')

def encender():
	print(colored("Encendiendo Firewall...", 'yellow'))
	time.sleep(1)
	os.system('systemctl enable firewalld && systemctl start firewalld')
	time.sleep(1)
	
def apagar():
	print(colored("Apagando Firewall...", 'yellow'))
	time.sleep(1)
	os.system('systemctl stop firewalld && systemctl disable firewalld')
	time.sleep(1)
	
# -------------------------------------------------------	

def Reload():
	print(colored("Cargando cambios...", 'yellow'))
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print(colored("Guardado", 'yellow'))
	time.sleep(2)
	os.system('clear')
	
# Agregar servicio ---------------------------------------

def addServ():
	print(colored("Escriba el servicio que desea agregar.", 'yellow'))
	print(colored('''--------------------''', 'blue'))
	servicio = input(colored("servicio: ", 'green'))
	os.system('clear')
	print(colored("Agregando servicio:", 'yellow'), servicio)
	time.sleep(1)
	os.system('firewall-cmd --zone=public --add-service='+servicio+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print("El servicio", servicio, "fue agregado correctamente, verificar:")
	time.sleep(1)
	print(colored('''------------------------------------------''', 'yellow'))
	os.system('firewall-cmd --list-all')

def remove():
	print(colored("Escriba el servicio que desea retirar del Firewall.", 'yellow'))
	print(colored('''--------------------''', 'blue'))
	servicio = input(colored("Servicio: ", 'green'))
	os.system('clear')
	print(colored("Removiendo servicio....", 'yellow'))
	time.sleep(1)
	os.system('firewall-cmd --zone=public --remove-service='+servicio+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print("El servicio", servicio, "ha sido removido con exito, verificar:")
	time.sleep(1)
	print(colored('''------------------------------------------''', 'yellow'))
	os.system('firewall-cmd --list-all')
	
# Agregar los puertos -----------------------------------

def addPuerto():
	print(colored("Escriba el Puerto que desea agregar.", 'yellow'))
	print(colored("Ejemplo: 445/tcp o 445/udp", 'cyan'))
	print(colored('''--------------------''', 'yellow'))
	puerto = input(colored("Puerto: ", 'green'))
	os.system('clear')
	print(colored("Agregando puerto....", 'yellow'))
	time.sleep(1)
	os.system('firewall-cmd --zone=public --add-port='+puerto+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print(colored('''------------------------------------------''', 'yellow'))
	print("El puerto", puerto, "ha sido agregado con exito, verificar:")
	time.sleep(1)
	print(colored('''------------------------------------------''', 'yellow'))
	os.system('firewall-cmd --list-all')
	
def removePuerto():
	print("Escriba el Puerto que desea remover.")
	print("Ejemplo: 445/tcp o 445/udp")
	print(colored('''--------------------''', 'yellow'))
	puerto = input(colored("Puerto: ", 'green'))
	os.system('clear')
	print(colored("Removiendo puerto....", 'yellow'))
	time.sleep(1)
	os.system('firewall-cmd --zone=public --remove-port='+puerto+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print(colored('''------------------------------------------''', 'yellow'))
	print("El puerto", puerto, "ha sido removido con exito, verificar:")
	time.sleep(1)
	print(colored('''------------------------------------------''', 'yellow'))
	os.system('firewall-cmd --list-all')

# Lista -------------------------------------------------

def lista():
	while True:
		print(colored("Enlistando servicios...", 'yellow'))
		time.sleep(1)
		print(colored('''------------------------------------------''', 'blue'))
		os.system('firewall-cmd --list-all')
		print(colored('''------------------------------------------''', 'blue'))
		print("Pulsa Enter/cualquiera para regresar")
		opcion = input("")
		os.system('clear')
		menu()


# MENUS --------------------------------------------------


def Agregar_puertos():
	while True:
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("Puertos", 'yellow'))
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Agregar un puerto")
		print(colored("[2]", 'yellow'), "Quitar un puerto")
		print(colored("[3]", 'yellow'), "Lista")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Regresar al menu")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			addPuerto()
		elif opcion == "2":
			removePuerto()
		elif opcion == "3":
			lista()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			menu()
			
		else:
			print(colored("Opción no valida", 'red'))
			time.sleep(2)
			os.system('clear')


def Agregar_servicio():
	while True:
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("Servicios", 'yellow'))
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Agregar un servicio")
		print(colored("[2]", 'yellow'), "Quitar un servicio")
		print(colored("[3]", 'yellow'), "Lista")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Regresar al menu")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			addServ()
		elif opcion == "2":
			remove()
		elif opcion == "3":
			lista()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			menu()
			
		else:
			print(colored("Opción no valida", 'red'))
			time.sleep(2)
			os.system('clear')


def Opciones_encendido():
	while True:
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("Opciones de encendido", 'yellow'))
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Status del Firewall")
		print(colored("[2]", 'yellow'), "Encender Firewall")
		print(colored("[3]", 'yellow'), "Apagar Firewall")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Regresar al menu")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			status()
		elif opcion == "2":
			encender()
		elif opcion == "3":
			apagar()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			menu()
			
		else:
			print(colored("Opción no valida", 'red'))
			time.sleep(2)
			os.system('clear')

		



def menu():
	while True:
		print(colored('''------------------------------------------''', 'blue'))
		print(colored("[1]", 'yellow'), "Opciones de encendido")
		print(colored("[2]", 'yellow'), "Agregar servicios")
		print(colored("[3]", 'yellow'), "Agregar puertos")
		print(colored("[4]", 'yellow'), "Cargar modificaciones")
		print(colored("[5]", 'yellow'), "Lista")
		print(colored('''--------------------''', 'yellow'))
		print(colored("[c]", 'magenta'), "Limpiar consola")
		print(colored("[0]", 'magenta'), "Salir")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input(colored("Selecciona una opción: ", 'green'))
		os.system('clear')
		
		if opcion == "1":
			Opciones_encendido()
		elif opcion == "2":
			Agregar_servicio()
		elif opcion == "3":
			Agregar_puertos()
		elif opcion == "4":
			Reload()
		elif opcion == "5":
			lista()
		elif opcion == "c":
			os.system('clear')
		elif opcion == "0":
			print(colored("Saliendo...", 'yellow'))
			time.sleep(1)
			os.system('clear')
			sys.exit()
			
		else:
			print(colored("Opción no valida", 'red'))
			time.sleep(2)
			os.system('clear')
		
		
		
		
if __name__ == '__main__':
    menu()



