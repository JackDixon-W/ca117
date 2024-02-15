#!/usr/bin/env python3

import sys

def moveA(cups):
  temp = cups[0]
  cups[0] = cups[1]
  cups[1] = temp
  return cups

def moveB(cups):
  temp = cups[1]
  cups[1] = cups[2]
  cups[2] = temp
  return cups

def moveC(cups):
  temp = cups[0]
  cups[0] = cups[2]
  cups[2] = temp
  return cups

start = sys.stdin.readline().strip()
moves = sys.stdin.readline().strip()

cups = ['', '', '']
cups[int(start) - 1] = 'prize'

for char in moves:
  if char == "A":
    cups = moveA(cups)
  elif char == "B":
    cups = moveB(cups)
  elif char == "C":
    cups = moveC(cups)
# I wrote it as shown below but Einstein can't handle
# Match, case statements
  """
  match char:
    case 'A': cups = moveA(cups)
    case 'B': cups = moveB(cups)
    case 'C': cups = moveC(cups)
  """

print(cups.index('prize') + 1)
