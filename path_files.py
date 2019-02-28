#!/usr/bin/env python

import os

evpath = os.environ['PATH']


for path in evpath.split(os.pathsep):
    print(f"{path}, ",len(os.listdir(path)))
