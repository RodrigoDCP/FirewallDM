# FirewallDM
FirewallDM or FWD-M is a tool designed to simplify the use of another tool called "Firewalld" on Ubuntu servers. Firewalld is a dynamic firewall for Linux systems that provides a set of tools to manage network traffic.

FirewallDM is a console/terminal-based "graphical user interface" for Firewalld that allows inexperienced users to easily manage firewall configuration. The program can be installed on Ubuntu systems via the command line using the "apt-get" package manager.

It is important to note that to use FirewallDM, some prerequisites need to be installed on the server, such as Python3, Pip, Colorama, and others that may not be available by default on your system.

Once installed, FirewallDM provides several options for managing the Firewalld tool, such as the ability to add services and ports, as well as update and monitor firewall configuration. Additionally, the program also provides useful information on the current state of the firewall and applied rules on the system.

In summary, FirewallDM is a useful tool for those who want to manage Firewalld configuration on Ubuntu servers in an easy and efficient way. With its intuitive graphical user interface and multiple management options, this program is an excellent choice for users who have no experience in administering firewalls on Linux systems.

![Texto alternativo de la imagen](IMG/V1.2/menu1.PNG)
![Texto alternativo de la imagen](IMG/V1.2/opciones2.PNG)
![Texto alternativo de la imagen](IMG/V1.2/servicios3.PNG)
![Texto alternativo de la imagen](IMG/V1.2/puestos4.PNG)

# Last update

The console graphical user interface has been improved to enhance the readability of the data and results presented. Efforts have been made to make the information more accessible, with a more intuitive and visually appealing layout.

Moreover, a great emphasis has been placed on optimizing system response times. Some processes that used to take up to 2 seconds, now run in just 1 second. This has been made possible by reducing certain processes and optimizing others, resulting in faster and more efficient performance. As a result, the end user experiences greater speed and agility in interacting with the system.

In summary, the last update has significantly improved both the user interface and the overall system performance, making it easier to use and much more efficient in data processing.

# Iinstallation Guide/Guia de instalación
Make sure you have an Ubuntu Server system without a graphical interface installed.
Open your system's terminal.

Clone the repository into your local directory using the following command:
```bash
git clone https://github.com/RodrigoDCP/FirewallDM.git
```

```bash
cd FirewallDM
```

```
./install.sh
```
This script will install all the necessary dependencies to run the Python code found in the repository.

Once the installation is complete, you can execute the code using the following command:
```bash
python3 fwd.py
```
That's it! You should now be able to run the code on your Ubuntu Server system without any issues.
