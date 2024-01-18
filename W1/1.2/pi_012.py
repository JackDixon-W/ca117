#!/usr/bin/env python3

import math
import sys

for line in sys.stdin:
  line = int(line.rstrip("\n"))
  print(f'{math.pi:.{line}f}')
