#!/usr/bin/python3
"""
Console for AirBnB clone
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Define the console"""
    intro = "Welcome to the AirBNB_clone console"
    prompt = "(hbnb)"
    file = None

    def do_quit(self, args):
        """To exit the console"""
        return True

    def do_EOF(self, args):
        """To exit the console with Ctrl+D"""
        print()
        return True
   

if __name__ == '__main__':
    HBNBCommand().cmdloop()
