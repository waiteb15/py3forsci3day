#!/usr/bin/env python
from datetime import datetime

def main():
    print(get_oldest())
    print(get_youngest())


def get_info(term):
    pres = {}
    with open('DATA/presidents.txt') as pres_in:
        for raw_lin in pres_in:
            info = raw_lin.rstrip().split(':')
            # ben likely did this cleaner
            if info[0] == str(term):
                pres = {
                    'name': info[2] + info[1],
                    'DOB': info[3],
                    'DOD': info[4],
                    "Birthplace": info[5] + ', ' + info[6],
                    "Termtime": info[7] + '--' + info[8],
                    "Party": info[9]
                }

    return pres


def get_oldest():
    age = 0
    with open('DATA/presidents.txt') as pres_in:
        for raw_lin in pres_in:
            info = raw_lin.rstrip().split(':')
            dob = info[3]
            eot = info[8]
            if eot == "NONE":
                eot = datetime.now().strftime("%Y-%m-%d")
            newage = _days_between(dob, eot)
            if newage > age:
                age = newage
                name = info[2] + " " + info[1]
    return name


def get_youngest():
    age = 100000
    with open('DATA/presidents.txt') as pres_in:
        for raw_lin in pres_in:
            info = raw_lin.rstrip().split(':')
            dob = info[3]
            bot = info[7]
            if bot == "NONE":
                bot = datetime.now().strftime("%Y-%m-%d")
            newage = _days_between(dob, bot)
            if newage < age:
                age = newage
                name = info[2] + " " + info[1]
    return name


def _days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


if __name__ == '__main__':
    main()