#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]



f0 = []
for f in fruits:
    f0.append(f.upper())

print("f0:",f0, '\n')

# more pythonic way
# [EXPR for VARS in Iterable if CONDITIONS ]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))