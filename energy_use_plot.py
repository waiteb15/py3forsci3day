#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

col_names = ['Desc',"1960","1965","1970","1975","1980","1985","1990","1991",
    "1992","1993","1994","1995","1996","1997","1998","1999","2000",
    "2001","2002","2003","2004","2005","2006","2007","2008","2009",
    "(R) 2010","2011"
]

df = pd.read_csv('DATA/energy_use_quad.csv',index_col = [0], names = col_names, )
#print(df.loc['Transportation':'Residential and commercial':2, :])

h = list(df.head(0))



plt.plot(h[:],df.iloc[0,:],label='Transporation')
plt.plot(h[:],df.iloc[2,:],label='Industrial')
plt.plot(h[:],df.iloc[4,:],label='Residential & Commercial')
plt.xticks(rotation=90)
plt.legend()
plt.show()