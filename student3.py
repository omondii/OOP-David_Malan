#!/usr/bin/python3
"""
Here, we'll use classes to create a student datatype.
Objects are created from classess. They are instances ofclasses.
With classes and oop, we can valiated entered data. It gives us more control over our data
   Methods - functions defined in a class
   Objects - Instance of a class
"""
class Student:
    """Initializing the contents of the class
    We add variables to objects.
    in initialization, self - can be named anything. It gives you a
    ccess to the just created object
    """
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError ("Wrong house")
        self.name = name
        self.house = house

        """To print using **print(student)** We have to introduce another special
        methods **__str__**
        After defining the str method, it will enable python to access and see
        all data as strings
        """
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


    """
    By using classes, we can now validate our data upon entry.  This was not possible
    with the previous methods. We can catch errors when they occur, check if the data 
    entered is what our program expects. This is done by caching and raising exceptions

    In the print statement, lets now try to print the student type and not have to go
    into the object and print individual elements.
    """
