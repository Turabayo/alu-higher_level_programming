#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print(f' the last digit {number}:the string is greater than 5')
elif number == 0:
    print(f'the last digit {number}: the string and is 0')
elif number < 0:
    print(f' the digit {number}: the string is less than 6 and not 0')   
