#!/usr/bin/env python

import sys

myFile = sys.argv[1]

with open(myFile, 'r') as f:
    print(f.readlines())



