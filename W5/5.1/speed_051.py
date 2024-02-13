#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

maxspeed = 0
for linenum in range(1, len(inp)):
  p = inp[linenum - 1].split(' ')
  c = inp[linenum].split(' ')
  pt = int(p[0])
  ps = int(p[1])
  ct = int(c[0])
  cs = int(c[1])
  curspeed = (cs - ps) // (ct - pt)
  if curspeed > maxspeed:
    maxspeed = curspeed
print(maxspeed)
