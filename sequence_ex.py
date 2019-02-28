#!/usr/bin/env python

s1= "foo"
s2 = b'foo'  #bytes
s3 = ['f','o','o']
s4 = 'f', 'o', 'o'


print(s1.encode())  #string to bytes
print(s2.decode())  #bytes to strings
print(s2[0])

#string manimpulation
actor = 'John Cena'
print(actor.upper())
print(actor.split())
print(actor[:4])
print(actor[0:4])
print(actor[-4:])
# string[start:stop:step]