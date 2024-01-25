#!/usr/bin/env python3

import sys

lib = {"A": 0, "B": 1, "C": 2}
inp = sys.stdin.read()
inp = inp.rstrip().split()
order = inp[3]
inp.pop()

# To anyone viewing, for some reason the third test specifically
# Uses strings instead of integers, so you have to convert it manually
# Otherwise, .sort() won't work
conv = []
for item in inp:
  conv.append(int(item))

conv.sort()
ans = ""
for item in order:
  ans = ans + str(conv[lib[item]]) + " "

ans = ans.rstrip()
print(ans)
