#!/usr/bin/python3
"""
Module the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class contine commands
    """
    prompt = '(hbnb)'
    my_classes = ["BaseModel", "eerwer"]

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
                    print(id)
                    return
            print("arregla eso")

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
