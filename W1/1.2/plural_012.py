#!/usr/bin/env python3

import sys

vowel = ["a", "e", "i", "o", "u"]

for line in sys.stdin:
  line = line.rstrip("\n")
  end = line[len(line) - 2:]
  fin = 0
  if end == "ch" or end == "sh" or end[1] == "x" or end[1] == "s" or end[1] == "z":
    fin = line + "es"
  elif end[0] not in vowel and end[1] == "y":
    fin = line[:len(line) - 1] + "ies"
  elif end[1] == "f":
    fin = line[:len(line) - 1] + "ves"
  elif end == "fe":
    fin = line[:len(line) - 2] + "ves"
  elif end[1] == "o":
    fin = line + "es"
  else:
    fin = line + "s"
  print(fin)
