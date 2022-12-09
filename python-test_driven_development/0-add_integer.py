#!/usr/bin/python3
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
