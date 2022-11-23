#!/usr/bin/python3
"""Module 1-hbtn_header.py
"""

import urllib.request
import urllib.parse
import sys


if __name__ == '_main__':

    url = sys.argv[1]
    message = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(message)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as reply:
        content = reply.read()
        print("{}".format(content.decode("utf-8")))
