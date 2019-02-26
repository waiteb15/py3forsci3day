#!/usr/bin/env python
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
                DOB = raw_lin[3]
                DOD = raw_lin[4]
                if DOD == 'NONE':
                    DOD = "***"
                Full_Name = raw_lin[2] + " " + raw_lin[1]

    if Full_Name != None:
        print(f"{Full_Name}: Born: {DOB}, Died: {DOD}")
    else:
        print(f"{last_name_in.upper()} not found: Try again...")