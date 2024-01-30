#!/usr/bin/env python3

import sys
inp = sys.stdin.readlines()

for line in inp:
  tstart = [num for num in range(1, int(line) + 1) if not num % 3]
  print(f'Multiples of 3: {tstart}')
  tsquare = [num*num for num in tstart]
  print(f'Multiples of 3 squared: {tsquare}')
  fstart = [num for num in range(1, int(line) + 1) if not num % 4]
  fdouble = [num*2 for num in fstart]
  print(f'Multiples of 4 doubled: {fdouble}')
  fORt = [num for num in range(1, int(line) + 1) if not num % 3 or not num % 4]
  print(f'Multiples of 3 or 4: {fORt}')
  fANDt = [num for num in fstart if num in tstart]
  print(f'Multiples of 3 and 4: {fANDt}')
