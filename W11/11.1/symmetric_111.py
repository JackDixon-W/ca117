#!/usr/bin/env python3

import sys

# Put them all into a dictionary
# Keys = length of words
# Values = a list of the words with that length
# Run through a loop printing the first name in the list
# Then run through a new loop printing the second name in the list
# Catch errors with list length and just continue past them (?)

pairs = {}
inp = sys.stdin.read().split('\n')
inp.pop()
for line in inp:
  pairs[len(line)] = list()

for name in inp:
  pairs[len(name)].append(name)

# We now have a dictionary
# Inside the dictionary are lists of all words of the same length

for word in pairs:
  print(f'{pairs[word][0]}')

for word in reversed(pairs):
  try:
    print(f'{pairs[word][1]}')
  except IndexError:
    continue
