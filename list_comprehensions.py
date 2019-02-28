#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]


f0 = []
for f in fruits:
    f0.append(f.upper())

print("f0:",f0, '\n')

# more pythonic way
# [EXPR for VARS in Iterable if CONDITIONS ]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

SUITS = 'Clubs Diamomnds Hearts Spades'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [ f'{r}-{s}' for s in SUITS for r in RANKS]
print(cards)
print('\n')

#generators
fgen = f1 = (f.upper() for f in fruits)
fruits.append('sour cherry')
print(fgen)
for f in fgen:
    print(f)

print(fgen)
#generator is empty
print("try printing generator again")
for f in fgen:
    print(f)

full_names = (f'{f} {l}' for f, l, _ in people)

print(full_names)
for f in full_names:
    print(f)