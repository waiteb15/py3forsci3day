#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

col_names = ['Desc', "1960","1965","1970","1975","1980","1985","1990","1991",
    "1992","1993","1994","1995","1996","1997","1998","1999","2000",
    "2001","2002","2003","2004","2005","2006","2007","2008","2009",
    "(R) 2010","2011"
]

df = pd.read_csv('DATA/energy_use_quad.csv', names = col_names, )
#print(df.loc['Transportation':'Residential and commercial':2, :])
print(df)
h = [float(f.lstrip('(R)')) for f in col_names[1:]]
plot_name = "Transportation, Industrial, Residential and Commercial".split(',')

for i, row in enumerate([0 , 2 , 4]):
    plt.plot([h:], df.iloc[row, 1:], label=df.loc[row,'Desc'])

# plt.plot(h[:],df.iloc[0,:],label='Transportation')
# plt.plot(h[:],df.iloc[2,:],label='Industrial')
# plt.plot(h[:],df.iloc[4,:],label='Residential & Commercial')
plt.xticks()
plt.xlabel("POWER")
plt.ylabel("YEAR")
plt.title("POWER USAGE!!!!")

plt.legend()
plt.show()

