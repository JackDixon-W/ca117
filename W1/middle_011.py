#!/usr/bin/env python3

import sys
for line in sys.stdin:
  if len(line) % 2 == 0:
    print(line[(len(line) // 2) - 1])
  else:
    print("No middle character!")
