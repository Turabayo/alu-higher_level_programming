#!/usr/bin/python3
#scripts that takes URL,Sends a request to the URL and displays the value of the X-request

import urllib.request
import sys

if__name__= "__main__":
    with urllib.request.urlopen(sys.argv[1] as res:
            print(res.headers.get('X-request-Id'))
