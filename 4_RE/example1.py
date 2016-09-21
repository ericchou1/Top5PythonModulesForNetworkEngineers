#!/usr/bin/env python

import re

# Open the file and break it into lines
with open('RTA_Config.txt', 'r') as f:
    #print(f.readlines())
    for line in f.readlines():
        print("This is line: " + line.strip())



