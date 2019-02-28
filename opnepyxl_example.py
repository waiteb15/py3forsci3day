#!/usr/bin/env python

import openpyxl as px


def main():
    wk = px.load_workbook('DATA/presidents.xlsx')
    ws =  wk["US Presidents"]

    for ws in wk:
        print(ws)

    ws = wk.active
    print(ws)


if __name__ == '__main__':
