#!/usr/bin/python3
"""
Module the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class contine commands
    """
    prompt = '(hbnb) '

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
