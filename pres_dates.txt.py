#!/usr/bin/env python

from datetime import datetime
def main():
    pres_age()

def _days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def pres_age():
    while True:
        last_name_in = input("Enter the last name of a President to get DOB and DOD (q for quit):").lower()
        Full_Name = None
        if last_name_in == 'q':
            break
        print(f"searching for {last_name_in}...")
        with open('DATA/presidents.txt') as pres_in:
            for raw_lin in pres_in:
                raw_lin = raw_lin.rstrip().split(':')
                if raw_lin[1][:len(last_name_in)].lower() == last_name_in:
                    dob = raw_lin[3]
                    dod = raw_lin[4]
                    if dod == 'NONE':
                        dod = datetime.now().strftime("%Y-%m-%d")
                    AGE = _days_between(dob, dod) // 365.25
                    Full_Name = raw_lin[2] + " " + raw_lin[1]

        if Full_Name != None:
            print(f"{Full_Name}: AGE: {AGE:.0f}")
        else:
            print(f"{last_name_in.upper()} not found: Try again...")

if __name__ == '__main__':
    main()