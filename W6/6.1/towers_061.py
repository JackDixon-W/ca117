#!/usr/bin/env python3

import sys

inp = sys.stdin.read().strip().split()

past = 0
towers = 0
for num in inp:
    if int(past) < int(num):
        towers += 1
    past = int(num)
print(towers)
