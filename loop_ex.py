#!/usr/bin/env python

while True:
    name = input("enter name or q to quit:")
    if name == 'q':
        break
    print("Processing {}...".format(name))

fruits = ['apple', 'orange', 'dragonfruit']
for f in fruits:
    print(f.upper())



target = 'x'
for f in fruits:
    if f.startswith(target):
        print(f"found {f}")
        break
else:  #if break isn't executed
    print("not found")