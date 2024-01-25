#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.rstrip().split()
  if len(line[0]) != len(line[1]):
    print("False")
    continue
  out = True
  count = 0
  for char in line[0]:
    if char in line[1]:
      line[1] = line[1].replace(char, "!", 1)
      count += 1
    else:
      out = False
  if out is True and count == len(line[1]):
    print(out)
  else:
    print("False")

