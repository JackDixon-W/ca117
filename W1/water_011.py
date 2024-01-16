#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
water = int(lines[0])
buckets = lines[1].split()

sum = 0
ans = 0
stop = False
for bucket in buckets:
  if sum + int(bucket) <= water and stop is False:
    ans += 1
    sum += int(bucket)
  else:
    stop = True

print(ans)
