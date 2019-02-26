#!/usr/bin/env python

for b in dir(__builtins__): #70ish built in functions
    if not b.startswith('__'):
        print(b)