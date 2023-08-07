# AirBnB Clone Command Interpreter

## Overview

This project is the first step towards building an AirBnB clone web application. The primary goal of this project is to create a command interpreter that will allow you to manage AirBnB objects. The command interpreter will help you create, retrieve, update, and delete instances of various classes that represent different entities within the AirBnB application.

## Project Goals

The main objectives of this project are as follows:

- Implement a parent class called `BaseModel` responsible for initialization, serialization, and deserialization of instances.
- Establish a simple flow of serialization and deserialization: Instance <-> Dictionary <-> JSON string <-> File
- Create multiple classes (User, State, City, Place, etc.) that inherit from the `BaseModel` class, representing different entities in the AirBnB application.
- Develop an abstracted storage engine named `FileStorage` for managing objects.
- Design and execute unit tests to validate the functionality of all classes and the storage engine.

## What is a Command Interpreter?

The Command Interpreter in this context is analogous to a simplified version of the Shell. It provides a specific set of commands to manage objects in the AirBnB project. With the Command Interpreter, you can:

- Create new objects (e.g., Users, Places)
- Retrieve objects from files or databases
- Perform operations on objects (e.g., counting, statistics)
- Update attributes of objects
- Delete objects

## Project Structure

The project consists of the following components:

- `models` directory: Contains Python classes representing different entities in the AirBnB application. These classes inherit from the `BaseModel` class and define their attributes and methods.
- `models/engine` directory: Contains the `file_storage.py` module, which implements the `FileStorage` class responsible for managing object storage and serialization.
- `tests` directory: Contains unit tests to validate the functionality of classes and the storage engine.

## Getting Started

To use the AirBnB Clone Command Interpreter, follow these steps:

1. Clone the project repository from [GitHub](https://github.com/jsuarez19/holbertonschool-AirBnB_clone).
2. Navigate to the project directory.
3. Run the command interpreter using the provided entry point script: `python console.py`.
4. Use the available commands to manage AirBnB objects.

## Project Dependencies

The project utilizes the following dependencies:

- Python: 3.11.4 or higher
- `cmd` module: Used for implementing the command interpreter.
- `json` module: Used for JSON serialization and deserialization.

