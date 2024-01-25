#!/usr/bin/env python3

import sys

# Einstein doesn't seem to be able to handle match
# Very annoying but I'm keeping this

logs = sys.stdin.readlines()
final = int(logs[len(logs) - 2].rstrip())
logs = logs[:len(logs) - 2]

trust = True
for linenum in range(0, len(logs), 2):
  match logs[linenum + 1].rstrip():
    case "higher":
      if int(logs[linenum]) < final:
        trust = False
    case "lower":
      if int(logs[linenum]) > final:
        trust = False

if trust is True:
  print("Bert can be trusted")
else:
  print("Bert is not to be trusted")

