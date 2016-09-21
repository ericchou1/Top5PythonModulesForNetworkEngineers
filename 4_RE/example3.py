#!/usr/bin/env python

import re

# introducing list comprehension and re.compile
patterns = [re.compile(p) for p in ['ip address', 'interface ']]

# look at the nested for loops
with open('RTA_Config.txt', 'r') as f:
    for line in f.readlines():
        for pattern in patterns: 
            if(re.search(pattern, line)):
                print(line.strip())
        



