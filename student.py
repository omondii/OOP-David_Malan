#!/usr/bin/python3
"""
Get student details. Add more functionality to this while learning OOP in python
"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from  {house}")


"""
   Define the get name and get house functions required by main
   Args:
        name - takes input from user
        House - users house, as input
"""


def get_name():
    """
       We can return the input immediately. Instead of declaring
       name and returning it.
    """
    return input('Name: ')


def get_house():
    return input('Houuse: ')



if __name__ == '__main__':
    main()
"""
In student1.py, We continue with this problem but follow a different root.
Thats the beauty of python
"""
