#!/usr/bin/env python3

import sys

# Whenever a vowel is encountered
# Remove the next two characters/Replace them with ''
vowels = ['a', 'e', 'i', 'o', 'u']

for line in sys.stdin.read().split('\n'):
  if line == '':
    continue
  i = 0
  out = line
  while i < len(out):
    char = out[i]
    if char in vowels:
      out = out[:i + 1] + out[i + 3:]
    i += 1
  print(f'{out}')

