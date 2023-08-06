#!/usr/bin/python3
"""
Console for AirBnB clone
"""


import cmd
import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Define the console"""
    prompt = "(hbnb)"
    file = None
    classes = {"BaseModel": BaseModel, "Amenity": Amenity, 
            "City": City, "Place": Place, "Review": Review, 
            "State": State, "User": User} 

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

    def do_create(self, args):
        """To create new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
        arg_list = args.split()
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        all_objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        elif key not in all_objects:
            print("** no instance found **")
        else:
            print(all_objects[key])

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
        arg_list = args.split()
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        all_objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        elif key not in all_objects:
            print("** no instance found **")
        else:
            del (all_objects[key])

    def do_all(self, args):
        if not args:
            print(all_objects)
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            result = []
            for k, v in all_objects.items():
                result.append(str(v))       
            print(result)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
