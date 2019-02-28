#!/usr/bin/env python

import numpy as np


r2 = np.linspace(100, 200, 500)

r2.shape = 5, 10, 10

r2 = r2 * 0.5

print(r2)