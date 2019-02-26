#!/usr/bin/env python
presnames = []
with open('DATA/presidents.txt') as pres_in:
    presnames = [f"{raw_lin.rstrip().split(':')[2]} {raw_lin.rstrip().split(':')[1]}" for raw_lin in pres_in]

pres1 = [f.upper() for f in presnames]
for f in pres1:
    print(f)

#generator
print("\n \n USE A GENERATOR")
p1 = pres1 = (f.upper() for f in presnames)
print(p1)
for f in p1:
    print(f)
