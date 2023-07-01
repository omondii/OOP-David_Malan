#!/usr/bin/python3
"""
   TUPLES:

   The student data in student.py can be packed and unpacked
   so that we have a function that gets the input from the user,
   packs it into varibles and returns the packed varible.
"""
def main():
    """
      name, house are the packed return values of get_student()
      name & house are packed and retuned as at a single point,
      python allows this.
    """
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    """
    prompt user for data needed. Pack the data and return it.
    Return values:
        name & house
    """
    name = input("Name: ")
    house = input("House: ")
    return (name, house)




if __name__ == "__main__":
    main()
"""
We are packing and unpaking the data into a tuple.
Tuples are immutable data types that are separated by commas and enclosed in ()
In the code above, we will make this changes:
1. In main
    - change name, house to student
    - In the print statement, access the tuple elements using index      ing
2. in get_student
    - Enclose the return values in (). Effectively storing its contents in a tuple.

Tuples are immutable - their values/content can't be changed.
Use tuples if values you are wot=rking with don't need to be changed at any point by the user or program.

This method can work with lists, where the return values are enclosed in [].
Lists are mutable hence they'll allow the data to be changed.

To access the contents of both `tuples()` and `lists[]` - We use []
ie: tuple_a[0] or list_a[0].
"""
