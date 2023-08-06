#!/usr/bin/python3
"""
Console for AirBnB clone
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Define the console"""
    prompt = "(hbnb)"
    file = None

    def do_quit(self, args):
        """To exit the console"""
        return True

    def do_EOF(self, args):
        """To exit the console with Ctrl+D"""
        print()
        return True
   
    def emptyline(self):
        """To do nothing when empty line is passed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
