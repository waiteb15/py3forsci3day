#!/usr/bin/env python


import sys
import os


#dir = sys.argv[1]
dir = '.'

for file in os.listdir(dir):
    print(file, os.path.getmtime(file))
    age=10551210662.081048
    if os.path.getmtime(file) <= age:
        oldest = file
        age = os.path.getmtime(file)

print(oldest)