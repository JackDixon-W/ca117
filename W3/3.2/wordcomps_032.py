#!/usr/bin/env python3

import sys

def vowelCheck(word):
  vowels = ['a', 'e', 'i', 'o', 'u']
  for char in word:
    if char in vowels:
      vowels.remove(char)
  if len(vowels) == 0:
    return True
  else:
    return False

words = sys.stdin.readlines()

shortest = [word for word in words if vowelCheck(word)]
print(f'Shortest word containing all vowels: {min(shortest, key=len).strip()}')

suffix = 'iary'
count = [word.strip() for word in words if word.strip().endswith(suffix)]
print(f'Words ending in iary: {len(count)}')

higheste = 0
for word in words:
  if word.count('e') + word.count('E') >= higheste:
    higheste = word.count('e') + word.count('E')
moste = [word.strip() for word in words if word.count('e') + word.count('E') == higheste]
print(f"Words with most e's: {moste}")
