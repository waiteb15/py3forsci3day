#!/usr/bin/env python

#                    Return Value
# lambda param-list: expression
# only use lambda's when you are passing functions

def doit(func):
    result = func()
    print(result)


def hello():
    return "HELLO"

#call back functions
doit(hello)

doit(lambda : "wombats!")


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "Blueberry", "lychee", "grape", "date" ]

print(sorted(fruits, key =lambda tre: tre.lower()))           #inline Anomonyus funciton


