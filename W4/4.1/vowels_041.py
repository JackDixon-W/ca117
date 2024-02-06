#!/usr/bin/env python3

import sys

inp = sys.stdin.read()
lib = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in inp:
  if char.lower() in lib:
    lib[char.lower()] += 1

lib = dict(sorted(lib.items(), key=lambda key:key[1],reverse=True))

# So turns out he wants the width to be dynamic based on the
# largest length number in the dictionary
# I am not pleased
width = 0
for key, value in lib.items():
  if width < len(str(value)):
    width = len(str(value))

for key, value in lib.items():
  print(f'{key} : {value:{width}}')
