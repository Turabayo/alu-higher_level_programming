#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(input("Please Enter the number:"))
please enter the number: 98
if number < 0:
    print('the number is negative')
elif number > 0:
    print('the number is positive')
elif number == 0:
    print('the number is zero')
else:
    print('Nothing')
