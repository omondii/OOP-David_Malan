#!/usr/bin/python3
"""
Reading and writting files in python:
open() returns a file object. It mostly uses 2 positional arguments
and one keyword argument
>>f = open('workfile', 'w', encoding="utf-8")
- The first arg is a string containing the filename
- The second arg is a string describing the way the file will be used:
   - 'r': file will only be read
   - 'w': file will be opened only for writing
   - 'a': opens the file for appending. New data is added to the end
   - 'r+': opens file for both reading and writting
- It is good practice to use the keyword with
  - with wraps the execution of a block with methods defined by a context manager
  - without using with, you have to call f.close()/home/omondii/OOP-David_Malan

Methods of File Objects
- File methods provide several methods for perfoming various operations on files.
*read() - Reads a files contents and returns it as a string.
    - read(size) - size is an optional numeric argument. When size is omitted/negative
                   the entire contents of the file will be read and returned.

*readline() - Reads a single line from the file
"""
def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file
    params:
       filename: name of the file to append
       text: the string to append
    Return:
       Number of characters added
    """
    with open(filename, encoding="utf-8") as f:
        """
        basic open function to open a file
        """
    with open(filename, mode='a', encoding="utf-8") as f:
        """
        append text to the end of a file
        "a" - append
        """
    with open(filename, mode="w", encoding="utf-8") as f:
        """
        open a file and write a string into it.
        "w" - write
        """
        f.write(text)
        return len(text)
