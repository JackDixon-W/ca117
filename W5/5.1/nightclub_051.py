#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
cap = int(inp[0])
inp = inp[1:]

inside = 0
stopped = 0
for line in inp:
  cur = line.split(" ")
  if cur[0] == "enter" and (inside + int(cur[1])) <= cap:
    inside += int(cur[1])
  elif cur[0] == "leave":
    inside -= int(cur[1])
  else:
    stopped += 1

print(stopped)
