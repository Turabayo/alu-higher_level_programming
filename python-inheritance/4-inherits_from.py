#!/usr/bin/python3
"""Prototype"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class \n that inherited (directly or indirectly) from the specified class or False)"""
return isinstance(obj, a_class) and type(obj) != a_class
