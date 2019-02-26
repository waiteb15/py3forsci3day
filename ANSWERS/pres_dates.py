#!/usr/bin/python

pres_lname = input("Enter president's last name: ")

with open("../DATA/presidents.txt") as PRES:
    for rec in PRES:
        flds = rec.split(":")
        if flds[1] == pres_lname:
            if flds[4] is None:
                alive = True
            else:
                alive = False
    
            print("NAME: {0} {1}".format( flds[2],flds[1] ))
            print("BIRTH: ", flds[3])
            print("DEATH: ",end='')
            if alive:
                print('* * *')
            else:
                print(flds[4])
