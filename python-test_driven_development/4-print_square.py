#!/usr/bin/python3
"""Define function"""


def print_square(size):
	"""function that prints a square"""
    if type(size) !=int:
	raise TypeError("size must be an integer")
    if type(size) < 0:
	raise TypeError("size must be >= 0")
    if size == 0:
	return
   else:
	for x in range(size)
	    print("#" * size)		

