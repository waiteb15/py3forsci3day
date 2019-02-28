#!/usr/bin/env python


dict = {}
with open('DATA/presidents.txt') as pres_in:
    for raw_lin in pres_in:
        raw_lin = raw_lin.rstrip().split(':')
        if dict.get(raw_lin[6], []) == []:
            dict[raw_lin[6]] = 1
        else:
            dict[raw_lin[6]] = dict[raw_lin[6]] + 1

for k, values in dict.items():
    print(f" {k}  {values}")