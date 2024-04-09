#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split('\n')

# Make a dictionary of all unique letters
# len(dic) = simplicity
# make a while loop that runs until len(dic) <= 2
# keep a tally of whenever a deletion occurs
# dic.get = the value of a key
# min(dic, key=dic.get) returns the key of the smallest value
# run a deletion on the smallest value until that value is 0

for line in lines:
  if line == '':
    continue
  simp = {}
  delCount = 0
  for char in line:
    if char in simp:
      simp[char] += 1
    else:
      simp[char] = 1
  while len(simp) > 2:
    toRem = min(simp, key=simp.get)
    simp[toRem] -= 1
    delCount += 1
    if simp[toRem] == 0:
      simp.pop(toRem)
  print(delCount)

