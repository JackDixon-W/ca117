#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
    if line.count("|") % 2 != 0:
        print("unsafe")
        continue
    count = 0
    for char in line:
        if char == "|":
            count += 1
        if char != "|":
            break
    if line.count("|") - count == count:
        print("safe")
    else:
        print("unsafe")
