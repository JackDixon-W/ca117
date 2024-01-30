#!/usr/bin/env python3

def even_squares(nums):
  out = [num*num for num in nums if not num % 2]
  return out

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_squares(numbers))
