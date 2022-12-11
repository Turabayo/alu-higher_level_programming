#!/usr/bin/python3
"""Define a function say my name"""


def say_my_name(first_name, last_name=""):
    """ A function that prints my name"""
    if type(first_name) != str:
       raise TypeError('first_name must be a string')
    if type(last_name) != str:
       raise TypeError('last_name must be a string')        	
    print('My name is {} {}'.format(first_name, last_name))
