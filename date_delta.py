#!/usr/bin/env python

import sys
from datetime import date, datetime, timedelta, time


#date = sys.argv[1]
#date = input("Enter date (YYYY-MM-DD):")
d1 = '1991-07-02'
#d1 = datetime.strptime(date, "%Y-%m-%d")
d2 = datetime.now().strftime("%Y-%m-%d")

def _days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

years = _days_between(d1,d2)//365.25
days = (_days_between(d1,d2) / 365.25 - years) * 365.25


print(f'{years:.0f} years and  {days:.0f} days')



