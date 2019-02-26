#!/usr/bin/env python
from sys import stdout
#Dont do this
def printa(*args, **kwargs): #generic function that accpets any number of arguments
    stdout.write("haha\n")


x = 100 # global


def spam():
    y= 42 # LOCAL
    print(f"x is {x}")
    print(f"y is {y}")
    return y


a = spam()
print(a)
printa(a)