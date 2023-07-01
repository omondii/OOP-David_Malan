#!/usr/bin/python3
"""
 In the previous solution we used tuples to tackle our problem,
 Now we'll use a dictionary.
 Dictionaries are a set pf key:value pairs.
 The key has to be unique
 We can acces its contet using the key.
 A dictionary is mutable and accessed using the key
"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")




def get_student():
    """
    Dictonaries are enclosed in {}. first line below
    initialize an empty dict.
    Here, student["name"] is the key & student["house"]is the value
    A dict is returned.
    """
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()


    """
    Cleaning the code:
    in get_student we don't have to declare the empty dict,
    get name and house as dictionaries. We can declare the
    variables name and house and store their values in a dict using
    the return.
    """
