#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  temp = line.capitalize()
  temp2 = line[len(temp) - 2]
  print(temp[:len(temp) - 2] + temp2.upper())

