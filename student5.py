#!/usr/bin/python3
"""
Getters and Setters:

Getter - A function for a class that gets some attribute
   To create a getter function; ** @property
    - The function is named exactly the way youd like it to be called.
Setter - A function for a class that sets some value
   To create a setter function, ** @house.setter
    -The seeter function will take 2 args; self and the object
    -The function name and variable name in setting getters and setters however
    can't be the same.
    -The convention to work around this is to place _ before the instance
     variables name in the setter and the getters return value
This 2 prevent manipulation of data by requirimg that inorder to get/set to some attribute you go through some function
We can now move our error checking from the init function to the setter function.
"""


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError ("Missing Name")
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError ("Wrong House!")
        self._house = house

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
We can access individual objects of a class using dot-notation
ie; in the main()
we can manipulate the data by doing this:
student.house = "A house". If we now run this, we will input data that meets the
validatio we did but it will print the value that we manipulated using
dot-notation.

Properties - attributes with more functionality. Prevents manipulation by giving
us more control.
Decorators - Functions that modify the behaviour of functions

By using getters and setters, the program will have a single point to access,
and set data into variables.
Values cant be manualy set.

The _ is not set in the init method. This is because if used, it will not use
the getter and setter methods.
"""
