#!/usr/bin/env python

import re

pattern = 'ip address' #assigning pattern into variable to be changed later

# Open the file and break it into lines
with open('RTA_Config.txt', 'r') as f:
    for line in f.readlines():
        # You can also just put the pattern into re.search as well
        if(re.search(pattern, line) or re.search('interface ', line)):
            print(line.strip())

        



