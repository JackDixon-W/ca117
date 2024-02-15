#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
  count = 1
  out = ''
  for charNum in range(len(line) - 1):
    if line[charNum] == line[charNum + 1]:
      count += 1
    else:
      out = out + str(count) + line[charNum]
      count = 1
  print(out)
