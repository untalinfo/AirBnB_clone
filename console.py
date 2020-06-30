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
            models.storage.reload()
            for key, value in models.storage.all().items():
                if value.id == my_id:
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
            my_id = str(args[1])
            models.storage.reload()
            new_dic = models.storage.all()
            for key, value in new_dic.items():
                if value.id == my_id:
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
        else:
            my_str = []
            my_id = str(args[1])
            models.storage.reload()
            new_dic = models.storage.all()
            for key, value in new_dic.items():
                if value.id == my_id:
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(args) == 3:
                        print("** value missing **")
                        return
                    else:
                        key = "{}.{}".format(args[0], args[1])
                        try:
                            obj = models.storage.all().get(key)
                            setattr(obj, args[2].replace('"', ''),
                                    args[3].replace('"', ''))
                            obj.save()
                        except:
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
