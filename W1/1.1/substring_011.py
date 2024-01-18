#!/usr/bin/env python3

import sys

for line in sys.stdin:
  lower = line.lower()
  temp = lower.split()
  if temp[0] in temp[1]:
    print("True")
  else:
    print("False")
