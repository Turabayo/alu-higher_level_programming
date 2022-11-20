#!/bin/bash
# curl sends GET req to URL, displays response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
