#!/usr/bin/python3
"""
This is the '5-test_identation' module.
The 5-text_identation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines long "?",":",".", followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == '':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")