#!/usr/bin/python3
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError ("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError ("Wrong House!")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    """Lets create a method that will return an emoji for each students patronus
    In implementing the patronous; we seee that we can call a metod outside of the    class, all class objects are indented below the class.
    Emojis are fonts
    """
    def charm(self):
        if self.patronus == "Stag":
            return "🐴"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russel terrier":
            return "🦊"
        else:
            return "🦴"

def main():
    student = get_student()
    print("Expecto patronus")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()


"""
The real power of classes and oop in general is the ability to create ad define
our own methods.
"""
