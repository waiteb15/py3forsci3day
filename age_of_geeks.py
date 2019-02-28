#!/usr/bin/env python

import openpyxl as px


def main():
     wb = px.load_workbook('DATA/computer_people.xlsx')
     ws = wb['people']
     print(f"Average age {get_average_age(ws):.0f}")



def get_average_age(ws):
    i = 0
    age = 0
    for row in ws['A2:D9']:
        if row[3].value != 'Deceased':
            age =  age + row[3].value
            i = i + 1
    return age/i


if __name__ == '__main__':
    main()