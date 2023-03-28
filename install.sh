#!/bin/bash

# Actualizar lista de paquetes e instalar paquetes necesarios
sudo apt update
sudo apt upgrade -y
sudo apt install -y python python3 python-pip python3-pip

# Instalar Colorama y Termcolor
pip install colorama termcolor
pip3 install colorama termcolor

# Instalar otras dependencias necesarias
sudo apt install -y python3-itertools python3-random

# Confirmar que la instalación ha finalizado
echo "La instalación ha finalizado correctamente"
