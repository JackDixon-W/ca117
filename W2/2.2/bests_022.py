#!/usr/bin/env python3

import sys

file = sys.argv[1]
highest = 0
full = []

try:
  with open(file, "r") as f:
    for line in f:
      if len(line) > 3 and int(line[:2]) >= highest:
        temp = highest
        highest = int(line[:2])
        if temp != highest:
          full = []
        full.append(line[2:].strip())
      else:
        continue
    names = ""
    for name in full:
      if names == "":
        names += name
      else:
        names += ", " + name
    print("Best student(s):", names)
    print("Best mark:", highest)
except FileNotFoundError:
  print(f'The file {file} could not be opened.')
