#!/usr/bin/env python3

import sys

def primeCheck(num):
  # If given number is greater than 1
  if num > 1:
      # Iterate from 2 to n / 2
      for i in range(2, int(num/2)+1):
          # If num is divisible by any number between
          # 2 and n / 2, it is not prime
          if (num % i) == 0:
              return False
      else:
          return True
  else:
    return False

inp = sys.stdin.readlines()

for line in inp:
  primes = [num for num in range(1, int(line)) if primeCheck(int(num))]
  print(f'Primes: {primes}')
