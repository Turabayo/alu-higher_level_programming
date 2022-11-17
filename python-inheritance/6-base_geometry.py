#!/usr/bin/python3
"""creating a geometry class"""


class BaseGeometry():
     """Represent base geometry."""

     def area(self):
         """Area of a geo"""
         raise Exception("area() is not implemented")
