#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
  cur = line.count('e')
  out = "h" + ('e' * cur * 2) + 'y'
  print(out)
