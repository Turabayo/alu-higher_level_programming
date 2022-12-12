 #!/usr/bin/python3
"""Defining a Text indentation function"""


def text_indentation(text):
    """A function that prints a text with 2 new lines"""
    if type(text) is not str:
       	raise TypeError("text must be a string")
    for x in ".?:":
        text = (x + "\n\n").join([j.strip(" ") for j in text.split(x)])
    print("{}".format(text), end="")	
