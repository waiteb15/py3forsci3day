#!/usr/bin/env python

import pandas as pd

from printheader import print_header

para_df = pd.read_csv('DATA/parasite_data.csv')
print(para_df.shape)
print(para_df.head())



min_val = 1.0
vals = para_df['ShannonDiversity'] >= min_val
print(para_df[vals])
