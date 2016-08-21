#!/usr/bin/env python

import sys

print("Please tell me your favorite color: ")
color = sys.stdin.readline()

animal = raw_input("Please tell me your favorite animal: ")
print(animal)

sys.stdout.write("Your favorite color is: " + color + " favorite animal is: " + animal + "\n")
print("*" * 10)


