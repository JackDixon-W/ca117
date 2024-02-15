#!/usr/bin/env python3

import sys
import string

alphabet = list(string.ascii_lowercase)

for line in sys.stdin.readlines():
  missing = alphabet[:]
  curline = line.lower()
  for char in curline:
    if char in missing:
      missing.remove(char)
  missPrint = ''.join(missing)
  print('pangram' if missing == [] else f'missing {missPrint}')
