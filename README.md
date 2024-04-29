AirBnB Clone - The Console

The console is the first segment of the AirBnB project at Holberton School, designed to manage objects for the AirBnB(HBnB) website through a command interpreter.
Functionalities:

    Create, retrieve, update, and destroy objects
    Perform operations on objects (count, compute stats, etc.)

Table of Contents

    Environment
    Installation
    File Descriptions
    Usage
    Examples
    Bugs
    Authors
    License

Environment

This project is tested on Ubuntu 14.04 LTS using Python3 (version 3.4.3).
Installation

    Clone this repository: git clone "https://github.com/alexaorrico/AirBnB_clone.git"
    Navigate to the AirBnb directory: cd AirBnB_clone
    Run the console interactively: ./console and enter commands
    Run the console non-interactively: echo "<command>" | ./console.py

File Descriptions

console.py - Entry point of the command interpreter.
List of commands supported:

    EOF, quit - Exit console
    <emptyline> - Overwrites default emptyline method and does nothing
    create - Create a new instance of BaseModel, save it (to the JSON file), and print the ID
    destroy - Delete an instance based on the class name and ID (save the change into the JSON file)
    show - Print the string representation of an instance based on the class name and ID
    all - Print string representation of all instances based or not on the class name
    update - Update an instance based on the class name and ID by adding or updating attribute (save the change into the JSON file)

models/ directory contains classes used for this project:

base_model.py - BaseModel class:

    __init__(self, *args, **kwargs) - Initialization
    __str__(self) - String representation
    save(self) - Update updated_at attribute with the current datetime
    to_dict(self) - Return a dictionary containing all keys/values of the instance

Inherited Classes:

    amenity.py
    city.py
    place.py
    review.py
    state.py
    user.py

/models/engine directory contains File Storage class:

file_storage.py - Serializes instances to a JSON file & deserializes back to instances

    all(self) - Return the dictionary __objects
    new(self, obj) - Set in __objects the obj with key <obj class name>.id
    save(self) - Serialize __objects to the JSON file (path: __file_path)
    reload(self) - Deserialize the JSON file to __objects

/tests directory contains all unit test cases:

test_base_model.py - Test cases for BaseModel and TestBaseModelDocs classes
## Usage
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit



## Bugs
No known bugs at this time. 

## Authors
<<<<<<< HEAD

Ishtiag Abbaker
Nader Albaire
=======
Ishtiag Abbaker- [Github]  (https://github.com/IshtiagAbbaker) 
Nader Albaire - [Github](https://github.com/Nader-Albaire)
>>>>>>> eb9a5605808ac95e071198eb1c9cb5294c279a91
## License
Public Domain. No copy write protection. 

Authors

Ishtiag Abbaker (https://github.com/IshtiagAbbaker) <ishtiagabdelmomen@gmail.com>
Nader Albaire (https://github.com/Nader-albaire) < nader.albaire@gmail.com>

## Additional Information:

    Contributions: Ishtiag Abbaker and Nader Albaire were the primary contributors to the initial development of the project. They spearheaded the creation of the command interpreter and laid the foundation for the subsequent segments of the AirBnB project at Holberton School.

    Project Progression: The AirBnB project at Holberton School is an ongoing endeavor, with subsequent segments building upon the work done in the console segment. The project aims to cover fundamental concepts of higher-level programming while progressively developing functionalities to replicate the AirBnB website.

    Collaboration: The development of the project involved collaboration among students and instructors at Holberton School, fostering a learning environment where students could exchange ideas, troubleshoot issues, and collectively work towards project milestones.

    Future Enhancements: As the project evolves, future enhancements may include additional functionalities, optimization of existing code, and integration of advanced features to mirror the full functionality of the AirBnB website.
