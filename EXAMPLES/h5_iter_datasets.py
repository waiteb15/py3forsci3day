#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

H5_DATASET = '/arrays/2D int8x9'

hfile = h5py.File(H5_FILE)

dset = hfile[H5_DATASET]

for i, row in enumerate(dset):
    print("ROW {}: {}".format(i, row))
print()

print("Row index 1 (second row):")
print(dset[1]) # second row
print()


print("Column index 1 (second column):")
print(dset[:,1:4])
print()

print("Rows 3 & 4, Columns 5 & 6")
print(dset[3:5, 5:7])

