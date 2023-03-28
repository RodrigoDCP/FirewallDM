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
print(colored("			version - 1", 'yellow'))


# [1] -----------------------------------------------

def status():
	print("Verificando estado del Firewall...")
	time.sleep(1)
	os.system('firewall-cmd --state')

def encender():
	print("Encendiendo Firewall...")
	time.sleep(1)
	os.system('systemctl enable firewalld && systemctl start firewalld')
	time.sleep(2)
	os.system('clear')

	
def apagar():
	print("Apagando Firewall...")
	time.sleep(1)
	os.system('systemctl stop firewalld && systemctl disable firewalld')
	time.sleep(2)
	os.system('clear')
# -------------------------------------------------------	

def Reload():
	print(colored("Cargando cambios...", 'yellow'))
	time.sleep(2)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print(colored("Guardado", 'yellow'))
	time.sleep(2)
	os.system('clear')
	
# Agregar servicio ---------------------------------------

def addServ():
	print("Escriba el servicio que desea agregar.")
	print(colored('''--------------------''', 'yellow'))
	servicio = input("servicio: ")
	os.system('clear')
	print("Agregando servicio", servicio)
	time.sleep(2)
	os.system('firewall-cmd --zone=public --add-service='+servicio+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print("El servicio", servicio, "fue agregado correctamente, verificar:")
	time.sleep(1)
	os.system('firewall-cmd --list-all')

def remove():
	print("Escriba el servicio que desea retirar del Firewall.")
	print(colored('''--------------------''', 'yellow'))
	servicio = input("Servicio: ")
	os.system('clear')
	print("Removiendo servicio....")
	time.sleep(2)
	os.system('firewall-cmd --zone=public --remove-service='+servicio+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print("El servicio", servicio, "ha sido removido con exito, verificar:")
	time.sleep(1)
	os.system('firewall-cmd --list-all')
	
# Agregar los puertos -----------------------------------

def addPuerto():
	print("Escriba el Puerto que desea agregar.")
	print("Ejemplo: 445/tcp o 445/udp")
	print(colored('''--------------------''', 'yellow'))
	puerto = input("Puerto: ")
	os.system('clear')
	print("Agregando puerto....")
	time.sleep(1)
	os.system('firewall-cmd --zone=public --add-port='+puerto+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print("El puerto", puerto, "ha sido agregado con exito, verificar:")
	time.sleep(1)
	os.system('firewall-cmd --list-all')
	
def removePuerto():
	print("Escriba el Puerto que desea remover.")
	print("Ejemplo: 445/tcp o 445/udp")
	print(colored('''--------------------''', 'yellow'))
	puerto = input("Puerto: ")
	os.system('clear')
	print("Removiendo puerto....")
	time.sleep(1)
	os.system('firewall-cmd --zone=public --remove-port='+puerto+' --permanent')
	time.sleep(1)
	os.system('firewall-cmd --reload')
	time.sleep(1)
	print("El puerto", puerto, "ha sido removido con exito, verificar:")
	time.sleep(1)
	os.system('firewall-cmd --list-all')
	

# MENUS --------------------------------------------------


def Agregar_puertos():
	while True:
		print(colored('''------------------------------------------''', 'blue'))
		print("Puertos")
		print(colored('''------------------------------------------''', 'blue'))
		print("[1] Agregar un puerto")
		print("[2] Quitar un puerto")
		print(colored('''--------------------''', 'yellow'))
		print("[c] Limpiar consola")
		print("[0] Regresar al menu")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input("Selecciona una opción: ")
		os.system('clear')
		
		if opcion == "1":
			addPuerto()
		elif opcion == "2":
			removePuerto()
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
		print("Servicios")
		print(colored('''------------------------------------------''', 'blue'))
		print("[1] Agregar un servicio")
		print("[2] Quitar un servicio")
		print(colored('''--------------------''', 'yellow'))
		print("[c] Limpiar consola")
		print("[0] Regresar al menu")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input("Selecciona una opción: ")
		os.system('clear')
		
		if opcion == "1":
			addServ()
		elif opcion == "2":
			remove()
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
		print("Opciones de encendido")
		print(colored('''------------------------------------------''', 'blue'))
		print("[1] Status del Firewall")
		print("[2] Encender Firewall")
		print("[3] Apagar Firewall")
		print(colored('''--------------------''', 'yellow'))
		print("[c] Limpiar consola")
		print("[0] Regresar al menu")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input("Selecciona una opción: ")
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
		print("[1] Opciones de encendido")
		print("[2] Agregar servicios")
		print("[3] Agregar puertos")
		print("[4] Cargar modificaciones")
		print(colored('''--------------------''', 'yellow'))
		print("[c] Limpiar consola")
		print("[0] Salir")
		print(colored('''------------------------------------------''', 'blue'))
		opcion = input("Selecciona una opción: ")
		os.system('clear')
		
		if opcion == "1":
			Opciones_encendido()
		elif opcion == "2":
			Agregar_servicio()
		elif opcion == "3":
			Agregar_puertos()
		elif opcion == "4":
			Reload()
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



