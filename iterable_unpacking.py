#!/usr/bin/env python

Values = [1,2,4,5, 6]

a, b, c, e, g = Values

print(a, b, c, e, g)

a, b, *c = Values
print(c)