#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.rstrip("\n")
  lib = {}
  count = 0
  for char in line:
    if char.isalpha() and char.islower():
      lib["lower"] = True
    elif char.isalpha():
      lib["upper"] = True
    elif char.isdigit():
      lib["digit"] = True
    else:
      lib["other"] = True
  for item in lib:
    count += 1
  print(count)
