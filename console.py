#!/usr/bin/python3
"""
Module the command interpreter
"""
import cmd
import models
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class contine commands
    """
    prompt = '(hbnb) '

    my_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                  'City': City, 'Place': Place, 'Amenity': Amenity,
                  'Review': Review}

    def do_quit(self, line):
        """
        Command quit, exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Command ctr + d, exit the program
        """
        return True

    def emptyline(self):
        """
        ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        args = str(line).split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            new_obj = HBNBCommand.my_classes.get(args[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        args = str(line).split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            my_id = str(args[1])
            my_k = args[0]
            models.storage.reload()
            for key, value in models.storage.all().items():
                if value.id == my_id and my_k == key.split('.')[0]:
                    print(value.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance
        """
        args = str(line).split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            my_k = args[0]
            my_id = str(args[1])
            models.storage.reload()
            new_dic = models.storage.all()
            for key, value in new_dic.items():
                if value.id == my_id and my_k == key.split('.')[0]:
                    del(new_dic[key])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances.
        """
        my_str = []
        args = line.split(' ')
        if len(line) == 0:
            list_string = []
            models.storage.reload()
            for key, value in models.storage.all().items():
                my_str.append(value.__str__())
            print(my_str)
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            new_dict = models.storage.all()
            for key, value in new_dict.items():
                if args[0] == key.split('.')[0]:
                    my_str.append(value.__str__())
            print(my_str)

    def do_update(self, line):
        """
        Update an instance
        """
        args = str(line).split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            match = 0
            my_k = args[0]
            my_id = str(args[1])
            models.storage.reload()
            new_dic = models.storage.all()
            for key, value in new_dic.items():
                if value.id == my_id and my_k == key.split('.')[0]:
                    print("** attribute name missing **")
                    match = 1
            if match == 0:
                print("** no instance found **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) == 4:
            my_k = args[0]
            m = 0
            my_id = str(args[1])
            models.storage.reload()
            new_dic = models.storage.all()
            for key, value in new_dic.items():
                if value.id == my_id and my_k == key.split('.')[0]:
                    m = 1
            if m == 1:
                key = "{}.{}".format(args[0], args[1])
                obj = models.storage.all().get(key)
                setattr(obj, args[2].replace('"', ''),
                        args[3].replace('"', ''))
                obj.save()
            if m == 0:
                print("** no instance found **")

    def default(self, args):
        a = args.split('.')
        if len(a) == 2:
            if a[1] == "all()":
                self.do_all(a[0])
            elif a[1] == "count()":
                count = 0
                my_dic = models.storage.all()
                for key, value in my_dic.items():
                    cl = str(key).split('.')
                    if a[0] == cl[0]:
                        count += 1
                print(count)
            elif a[1].split("(")[0] == "show":
                my_id = a[1].replace('show("', '')
                my_id = my_id.split('"')[0]
                my_str = a[0] + " " + my_id
                self.do_show(my_str)
            elif a[1].split("(")[0] == "destroy":
                my_id = a[1].replace('destroy("', '')
                my_id = my_id.split('"')[0]
                my_str = a[0] + " " + my_id
                self.do_destroy(my_str)
            elif a[1].split("(")[0] == "update":
                if "{" not in a[1]:
                    my_id = a[1].replace('update("', '')
                    spt = my_id.split('"')
                    my_id = spt[0]
                    my_arg = spt[2]
                    my_value = '"' + spt[4] + '"'
                    my_str = a[0] + " " + my_id + " " + my_arg + " " + my_value
                    self.do_update(my_str)
                else:
                    my_fr = a[1].replace('update("', '')
                    my_i = my_fr.split('", {')[0]
                    my_dic = my_fr.split('", {')[1]
                    my_dic = "{" + my_dic[:-1]
                    my_dic = eval(my_dic)
                    str_n = a[0] + " " + my_i
                    for key, value in my_dic.items():
                        parameter = str_n + " " + key + " " + str(value)
                        self.do_update(parameter)

    def help_quit(self):
        """
        provides information from the quit command
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """
        provides information from the EOF command
        """
        print("Exit to the console\n")

    def help_create(self):
        """
        Create a new instance
        """
        print("Creates a new instance of BaseModel, saves "
              "it (to the JSON file) and prints the id.\n"
              "Ex: $ create BaseModel\n")

    def help_show(self):
        """
        Print the string based in id
        """
        print("Prints the string representation of an"
              "instance based on the class name and id.\n"
              "Ex: $ show BaseModel 1234-1234-1234.\n")

    def help_destroy(self):
        """
        Delete instance
        """
        print("Deletes an instance based on the class"
              "name and id (save the change into the JSON file).\n"
              "Ex: $ destroy BaseModel 1234-1234-1234.")

    def help_all(self):
        """
        String representation of all instances
        """
        print("Prints all string representation of all"
              "instances based or not on the class name.\n"
              "Ex: $ all BaseModel or $ all.")

    def help_update(self):
        """
        Updates an instance
        """
        print("Updates an instance based on the class name and id by "
              "adding or updating attribute.\n"
              "Ex: $ update BaseModel 1234-1244-1234 name "'"First name"')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
