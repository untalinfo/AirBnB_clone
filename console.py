#!/usr/bin/python3
"""
Module the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
import shlex 


class HBNBCommand(cmd.Cmd):
    """
    This class contine commands
    """
    prompt = '(hbnb)'
    my_classes = ["BaseModel", "Place", "State", "City", "Amenity", "Review"]

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
            new_obj = BaseModel()
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
        args = str(line).split(' ')
        if len(line) == 0:
            list_string = []
            models.storage.reload()
            new_dict = models.storage.all()
            for key, value in new_dict.items():
                print(value.__str__())
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            new_dict = models.storage.all()
            for key, value in new_dict.items():
                print(value.__str__())

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
                            setattr(models.storage.all()[key], args[2], args[3])
                            models.storage.save()
                        except:
                            print("** no instance found **")
  
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
