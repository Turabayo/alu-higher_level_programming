#!/usr/bin/python3
"""Defining Unittest function"""


def max_integer(list=[]):

"""
    write unittests for the function def max_integer(list=[])
   Your test file should be inside a folder tests
   You have to use the unittest module
   Your test file should be python files (extension: .py)
   Your test file should be executed 
   All tests you make must be passable by the function below
"""
  if len(list) == 0:
     return None
 result = list[0]
 x=1
while x < len(list):
	if list[x] > result:
	   result = list[x]
	x += 1
return result
