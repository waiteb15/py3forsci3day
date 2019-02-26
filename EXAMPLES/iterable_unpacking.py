#!/usr/bin/env python
# (c)2015 John Strickler

values = ['a', 'b', 'c']

x, y, z = values

print(x, y, z)
print()

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]

for row in people:
    first_name, last_name, _  = row
    print(first_name, last_name)
print()

for first_name, last_name, _ in people:
    print(first_name, last_name)
print()
