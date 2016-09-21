#!/usr/bin/env python

import re

# introducing list comprehension and re.compile
patterns = [re.compile(p) for p in ['ip address', 'interface ']]

# Now iterate thru all the configs in the current direcotry
configs = ['RTA_Config.txt', 'RTB_Config.txt']
for config in configs:
    print("Opening: " + config)
    with open(config, 'r') as f:
        for line in f.readlines():
            for pattern in patterns: 
                if(re.search(pattern, line)):
                    print(line.strip())
    print("*" * 10)

        



