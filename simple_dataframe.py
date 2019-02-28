#!/usr/bin/env python

import pandas as pd
import numpy as np
cols = "Test1 Test2 Test3 Test4 Test5 Test6".split()

df = pd.DataFrame(np.random.randn(10, 6),columns=cols)
print('-' * 60 )
print('a')
print('-' * 60 )

print(df[['Test3','Test5']])
print('-' * 60 )
print('b')
print('-' * 60 )
print(df * 3)