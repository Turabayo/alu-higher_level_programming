#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(input("Please Enter the number: "))
if number < 0:
    print('the number is negative')
elif number > 0:
    print('the number is positive')
elif number == 0:
    print('the number is zero')
else:
    print('Nothing')
