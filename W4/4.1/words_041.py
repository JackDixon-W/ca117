#!/usr/bin/env python3

import sys
import string

inp = sys.stdin.read().split()

lib = {}
for word in inp:
  word.strip()
  word = word.strip(string.punctuation).lower()
  try:
    lib[word] += 1
  except KeyError:
    lib[word] = 1

lib = dict(sorted(lib.items()))
for key, item in lib.items():
  print(f'{key} : {item}')
