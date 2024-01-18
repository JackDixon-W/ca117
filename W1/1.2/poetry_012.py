#!/usr/bin/env python3

#Biggest line is 50 long
import sys

inp = sys.stdin.readlines()

highest = 0
for line in inp:
  line = line.rstrip("\n")
  if len(line) > highest:
    highest = len(line)

for line in inp:
  line = line.rstrip("\n")
  print(f'{line: ^{highest}}')
