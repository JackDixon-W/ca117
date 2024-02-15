#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
  linesplit = line.rstrip().split(' ')
  uniquenums = [num for num in linesplit if linesplit.count(num) == 1]
  try:
    print(max(uniquenums))
  except ValueError:
    print("none")
