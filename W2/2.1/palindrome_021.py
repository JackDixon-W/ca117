#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.rstrip().lower()
  for char in line:
    if char.isascii() and not char.isalpha() and not char.isdigit():
      line = line.replace(char, "")
  check = True
  for char in range(len(line) // 2):
    if line[char] != line[-char-1]:
      check = False
  print(check)
