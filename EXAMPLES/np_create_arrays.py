#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


# from nested sequences
a_nest = np.array([[1,2,3],[4,5,6],[7,8,9],[20,30,40]])
print(a_nest)
print("# dims", a_nest.ndim)
print("shape", a_nest.shape)
print()

# with zeros
a_zeros = np.zeros([3,5])
print(a_zeros)
print()

# with ones
a_ones = np.ones([2,3,4,5])
print(a_ones)
print()

# with uninitialized values
a_empty = np.empty([3,8])
print(a_empty)


a_empty[:] = np.NaN
print(a_empty)

#interval between
r1 = np.arange(50)
print("hello\n",r1)
print(r1.ndim)

#number of items
r2 = np.linspace(-10, 10, 100)
print(r2)
plt.plot(r2)

