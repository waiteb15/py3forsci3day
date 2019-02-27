#!/usr/bin/env python

import csv


with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)  #generator of the file
    for row in rdr:
        term, first, last, birthplace, birth_state, party = row
        term = int(term)
        print(term)
