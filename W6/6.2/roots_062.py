#!/usr/bin/env python3

import sys
import math

def findRoots(a, b, c):
  """
  Finds the roots of a given quadratic
  Calculates top and bottom parts of equation separate
  """
  try:
    Plus = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    Minus = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return [Plus, Minus]
  except ValueError:
    return None

for line in sys.stdin.readlines():
  cur = line.rstrip().split()
  roots = findRoots(int(cur[0]), int(cur[1]), int(cur[2]))
  try:
    print(f'{min(roots):.1f}, {max(roots):.1f}')
  except TypeError:
    print("None")
