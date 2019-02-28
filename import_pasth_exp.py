#!/usr/bin/env python

import os
import sys

FOLDER = 'DATA'
FILENAME = 'mary.txt'

print(os.sep)
print(sys.platform)

file_path=os.path.join(FOLDER,FILENAME)
print("file_path:",file_path)

print(os.path.dirname(file_path))

print(os.path)

