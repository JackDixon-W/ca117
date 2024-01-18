#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
for x in inp:
  temp = x[1:len(x) - 2]
  if temp != '':
    print(x[1:len(x) - 2])

