#!/usr/bin/env python3

import sys
for line in sys.stdin:
  temp = line.split("@")
  cur = temp[0]
  i = len(cur) - 2
  while cur[i].isdigit():
    i -= 1
  cur = cur[:i + 1]
  cur = cur.replace(".", " ")
  print(cur.title())
