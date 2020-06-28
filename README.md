# AirBnB_clone - Console

<img src="https://i.ibb.co/wRfsyTT/the-console.png" alt="Airbnb-the_console" border="0">

Welcome to the AirBnB clone project! (The Holberton B&B)

This project is a clone of Airbnb console

This project allows through a simple console (command interpreter) to create a data model. through the console you can create, update, destroy, etc. objects in JSON files. which allows a persistence of files to later be connected to the front-end.

# Table of Contents
1. [Requeriments](#requeriments-)
2. [How to use](#how-to-use-it-)
3. [Test](#test-%EF%B8%8F)
4. [Execute commands](#execute-commands-%EF%B8%8F)
5. [Development environment](#development-environment-%EF%B8%8F)
6. [Authors](#authors%EF%B8%8F)

## Requeriments 📋

Airbnb was built and tested in Ubuntu 14.04 LTS via Vagrant in VirtualBox. Programming languaje python3

## How to use it 🔧
Do you need clone this repository:
```
	git clone https://github.com/somarae8/AirBnB_clone
```
and then you can enter the folder of project:
```
	cd Airbnb_clone
```
after you can excecute with this command:
```
	./console.py
```
## Test ⚙️
Some examples of how to used this console:
### interactive mode:
```
vagrant@vagrant-ubuntu-trusty-64:~/Airbnb_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
============================================
EOF  help  quit  show  all  update  destroy

(hbnb) 
(hbnb) 
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/Airbnb_clone$
```
### non-interactive mode:
```
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$ cat test_help
help
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$ |
```
## Execute commands ⌨️
```
Command | Syntax | Output
------- | ------ | ------
help | `help [option]` | Displays all available commands
quit | `quit` | Exit command interpreter
EOF | `EOF (ctrl + d)` | Exit command interpreter
create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id
```
## Development environment 🛠️
This project has been tested on Ubuntu 14.06.6 LTS

* Programming languaje Python
* The tests are carried out in [virtualBox](https://www.virtualbox.com)
* Development environment manager [vagrant](https://www.vagrantup.com)
* Style guidelines: PEP 8 (version 1.7) || Google Style Python Docstrings

## Authors✒️
* Eduardo Ramos - student at Holberton School
* Oscar Eduardo Info - student at Holberton School

You can also look at the list of all [contributors](https://github.com/somarae8/AirBnB_clone/graphs/contributors) who have participated in this project.