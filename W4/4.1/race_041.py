#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

finname = ""
finmins = 61
finseconds = 61
for line in lines:
  cur = line.split()
  name = cur[0]
  cur = cur[1:]
  oldseconds = finseconds
  oldmins = finmins
  oldname = finname
  try:
    for time in cur:
      timesplit = time.split(":")
      if finmins > int(timesplit[0]):
        finmins = int(timesplit[0])
        finseconds = int(timesplit[1])
        finname = name
      elif finmins == int(timesplit[0]) and finseconds > int(timesplit[1]):
        finseconds = int(timesplit[1])
        finname = name
  except ValueError:
    finseconds = oldseconds
    finmins = oldmins
    finname = oldname

print(f'{finname} : {finmins}:{finseconds:0>2d}')
