#!/usr/bin/env python

x = 5

print(x)

#variables don't change this tuff
things = [1,2,3]
t = things
t.append(4)
print(things)

#can reassign variables so be cafeful
print(type(t))
t = 42
print(type(t))

#if i need it but can't define it yet
m = None