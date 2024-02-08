#!/usr/bin/env python3

import sys

inp = sys.stdin.read()
file = sys.argv[1]

with open(file, 'r') as file:
  file_contents = file.readlines()

trans = {}
for line in file_contents:
  cur = line.split(" ")
  trans[cur[0]] = cur[1].rstrip()
lib = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

nums_lines = inp.split("\n")
for line in nums_lines:
  nums = line.split(" ")
  out = ""
  for num in nums:
    num.strip()
    if not num.isnumeric():
      continue
    translation = trans[lib[int(num)]]
    out = out + translation + " "
  if len(out) > 2:
    print(out[:-1])
