#!/usr/bin/env python3

import sys
inp = sys.stdin.readlines()

# Return n if n is a multiple of 3
# Else, return 0
def helper(n):
  if n % 3:
    return 0
  else:
    return n

for line in inp:
  start = [helper(num) for num in range(1, int(line) + 1)]
  print(f'Non-multiples of 3 replaced: {start}')
