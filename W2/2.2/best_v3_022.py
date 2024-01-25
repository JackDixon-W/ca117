#!/usr/bin/env python3

import sys

file = sys.argv[1]
highest = 0

try:
  with open(file, "r") as f:
    for line in f:
      try:
        if len(line) > 3 and int(line[:2]) > highest:
          highest = int(line[:2])
          full = line[3:].rstrip()
        else:
          continue
      except ValueError:
        print(f'Invalid mark {line[:2]} encountered. Skipping.')
    print("Best student:", full)
    print("Best mark:", highest)
except FileNotFoundError:
  print(f'The file {file} could not be opened.')
