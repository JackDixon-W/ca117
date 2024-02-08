#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

nums = inp[0].split()
order = inp[1]

# Assign A : num[0]
# Etc.
# for char in line:
# lib[char] (which means num[whatever])
# List is now sorted
nums = sorted(nums)

# Manually building a library
# Very unnecessary but my head feels scrambled so we ball
lib = {"A": nums[0], "B": nums[1], "C": nums[2], "D": nums[3], "E": nums[4], "F": nums[5]}

out = ""
for char in order:
  try:
    out = out + lib[char] + " "
  except KeyError:
    continue
print(out[:-1])
