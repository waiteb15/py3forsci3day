#!/usr/bin/env python
import h5py
import matplotlib.pyplot as plt

H5_FILE = 'DATA/example.h5'

hfile = h5py.File(H5_FILE)

for group in hfile:
    print(group)

for data in hfile['Animals']:
    print(data)

H5_DATA = '/Animals/observations'
dataset = hfile[H5_DATA]
print(dataset)
print(dataset[:])

plt.figure(figsize=(5,3))
plt.plot(dataset[:,0],dataset[:,1])
plt.title('Animal Observations')
plt.suptitle("Trial")
plt.xlabel('Number')
plt.ylabel('Value')

plt.figure(figsize=(5,3))
plt.plot(dataset[:,0],dataset[:,1])
plt.title('Animal Observations')
plt.xlabel('Number')
plt.ylabel('Value')
plt.show()