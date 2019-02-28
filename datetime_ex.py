#!/usr/bin/env python

from datetime import date, datetime, timedelta, time


today = date.today()
print(today, today.year)

jack_bd = date(2018, 2, 23)

delta = today - jack_bd

years = delta.days // 365.25
print(f"Jack is {years:.0f} year/years old")

event = datetime(2019, 5, 11, 13, 22, 17)
ten_years = timedelta(10 * 365.25)

print(jack_bd + ten_years)


from dateutil.parser import parse

