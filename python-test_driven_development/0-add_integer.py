#!/usr/bin/python3
<<<<<<< HEAD
""" a function that adds 2 integers"""


def add_integer(a, b=98):


    """Write a function that adds 2 integers
        a and b must be integers or floats,
        otherwise raise a TypeError exception
        with the message a must be an integer 
        or b must be an integer"""
    if type(a) !=float and type(a) !=int:
        errorA = "a must be an integer"
        raise TypeError(errorA)
    elif type(b) != float and type(b) !=int:
        errorB = "b must be an integer"
        raise TypeError(errorB)
    return int(a)+ int(b)   
=======
# a function that adds 2 integers
"""
    define function 'add_integer'
"""


def add_integer(a, b=98):
    """
        this function return s the sum of two integers
    """
    if type(a) != float and type(a) != int:
        raise TypeError('a must be an integer')
    if type(b) != float and type(b) != int:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
>>>>>>> 958063eb1b70219a721a244991b6624f61368752
