#!/usr/bin/env python

try:
    with open('womb.txt') as wp_in:
        pass
except IOError as err:
    print(err)

print("DONT")