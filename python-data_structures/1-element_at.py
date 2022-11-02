#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]


a = [1, 2, 3, 4, 5]
print(element_at(a, 44444))
