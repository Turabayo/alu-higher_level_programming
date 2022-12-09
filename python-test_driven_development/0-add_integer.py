#!/usr/bin/python3
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
