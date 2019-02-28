#!/usr/bin/env python
import os

start_dir = "."


for curr_d, dirlist, filelist in os.walk(start_dir):
    if ".git" in curr_d:
        continue
    print(curr_d)
    for file_name in filelist:
        if file_name.endswith('.py'):
#            print(f"\t {file_name}")
            file_path = os.path.join(curr_d,file_name)
            file_size = os.path.getsize(file_path)
            print(f"\t {file_size:4d} {file_name}")