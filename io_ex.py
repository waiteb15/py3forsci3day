#!/usr/bin/env python

import getpass

name = 'anne'
color ='red'
val = 27


print(name, color, val)
print(name, color, val, sep='.')
print(f"My name is {name} and fav color is {color}")
print('name', end="=>") #no carriage retrun, \n is by default
print(name)

# must remember to open and close
mary_in = open('DATA/mary.txt') #file object #personal preference to _in for reading and _out for outptu
for raw_lin in mary_in:
    raw_lin= raw_lin.rstrip()
    print(raw_lin)
mary_in.close()

#opens and closes
with open('DATA/mary.txt') as mary_in:
    for raw_lin in mary_in:
        raw_lin = raw_lin.rstrip()
        print(raw_lin)

print("***READ***")
with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(contents)

with open('DATA/mary.txt') as mary_in:
    lines = mary_in.readlines()  #bad for larger files as all lines get loaded to memory

fruits = ['apple', 'orange', 'dragonfruit']
with open('fruits.txt', 'w') as fruits_out:
   for fruit in fruits:
        fruits_out.write(fruit + '\n')

#ask user
full_name = input("Pleas enter your full name?")
names = full_name.split()
if (len(names) < 2):
    full_name = input("thats not your full name, try again:")

#password stuff
#password = getpass.getpass("Enterpassword:")