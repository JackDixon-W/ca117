#!/usr/bin/env python3

import sys

logs = sys.stdin.readlines()
final = int(logs[len(logs) - 2].rstrip())
logs = logs[:len(logs) - 2]

trust = True
for linenum in range(0, len(logs), 2):
  temp = logs[linenum + 1].rstrip()
  if temp == "higher":
    if int(logs[linenum]) > final:
      trust = False
  elif temp == "lower":
    if int(logs[linenum]) < final:
      trust = False
  else:
    print("ERROR")

if trust is True:
  print("Bert can be trusted")
else:
  print("Bert is not to be trusted")

