#!/usr/bin/env python3

import sys
for line in sys.stdin:
  ans = line.replace("m", "M", 1)
  print(ans.rstrip())
