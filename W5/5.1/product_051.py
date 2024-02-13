#!/usr/bin/env python3

import sys

num = int(sys.stdin.read().strip())

# This list is used to hold all the values that
# Are to be multiplied together
tomult = []

while num >= 10:
  # Integers aren't iterable
  strnum = str(num)
  tomult = [int(char) for char in strnum if char != '0']
  newnum = 1
  for num in tomult:
    newnum = newnum * num
  num = newnum
print(num)
