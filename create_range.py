#!/usr/bin/env python
import numpy as np


a = np.arange(35)
a.shape = 5, 7

print(a)

a.shape = 7, 5

print(a)

