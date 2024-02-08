#!/usr/bin/env python3

import sys

inp = sys.stdin.read()
lib = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero', 100: 'one hundred'}
# lib = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

nums_lines = inp.split("\n")
for line in nums_lines:
  nums = line.split(" ")
  out = ""
  for num in nums:
    num.strip()
    if not num.isnumeric():
      continue
    try:
      out = out + lib[int(num)].lower() + " "
    except KeyError:
      try:
        out = out + lib[int(num)-(int(num)%10)].lower() + "-" + lib[int(num)%10].lower() + " "
      except KeyError:
        continue
  if len(out) > 2:
    print(out[:-1])
