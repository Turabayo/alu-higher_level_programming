#!/usr/bin/python3



class MyList(list):
    """Inheritance form superclass"""

def print_sorted(self):
    """returns list in sorted order"""
    s_list = self[:]
    s_list.sort()
    print("{}".format(s_list))
