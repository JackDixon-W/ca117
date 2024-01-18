#!/usr/bin/env python3

import sys

for line in sys.stdin:
  check = True
  cur = line.lower()
  cur = cur.split()
  for char in cur[0]:
    if char in cur[1]:
      cur[1] = cur[1].replace(char, "!", 1)
    else:
      check = False
  print(check)
