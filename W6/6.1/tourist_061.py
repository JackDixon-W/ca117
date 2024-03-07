#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
entryLength = inp[0]
check = inp[-1].rstrip().split()

# Trim the lines we're dealing with to only relevant ones
inp = inp[1:-1]

visits = []
for line in inp:
    cur = line.rstrip().split()
    if cur[0] in check:
        visits.append(int(cur[1]))

if check[1] != "1":
    print(visits[int(check[1])])
else:
    print(visits[0])
