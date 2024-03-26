#!/usr/bin/env python3

import sys
import string

usedWords = {}

for line in sys.stdin.readlines():
  out = ''
  for word in line.strip().split():
    noPunc = word.translate(str.maketrans('', '', string.punctuation))
    if word.lower() not in usedWords and noPunc.lower() not in usedWords:
      out += word + ' '
      usedWords[noPunc.lower()] = True
    else:
      out += '. '
  print(out.strip())
