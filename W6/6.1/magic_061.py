#!/usr/bin/env python3

import sys
cur = int(sys.stdin.read().rstrip())

def magicCheck(number):
    digits = list(str(number))
    total = 0
    for num in digits:
        total += int(num)
    if number % total == 0:
        return True
    return False

while magicCheck(cur) is False:
   cur += 1 
print(cur)
