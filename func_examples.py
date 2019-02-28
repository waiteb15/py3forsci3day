#!/usr/bin/env python
"""
    function play
"""
def main():
    hello()
    a = get_message()
    print(a)
    s = Spam()
    greet_person(2)
    greet_person()
    greet_people1("mom","dad","bubble")
    greet_people2(["hello","bobby"])
    greet_people1(*["hello","bobby"]) # * unpacks the list to argument

class Spam():
    pass

#Display Logic
def hello():
    print("Hello, world")

# Business Logic
def get_message():
    return "Hello, world"

def greet_person(whom='world'):
    print("hello,", whom)

def greet_people1(*whom):
    for person in whom:
        print(f"hello, {person}")

def greet_people2(whom):
    for person in whom:
        print(f"hello, {person}")

def process_file(*,file_name, file_type): #* is a placeholder for the named arguments
    pass

def config(**stuff):
    print(stuff)
    print()

if __name__ == '__main__':
    main()
    process_file(file_name="foo.hd5",file_type="HDF")  # order doesn't matter for named parameters
    config(animal="wom", weapon = "cup", place = "hole")
