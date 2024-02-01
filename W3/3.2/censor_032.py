#!/usr/bin/env python3

import sys
'''
censor_file = sys.argv[1]
inp = sys.stdin.readlines()

with open(censor_file) as f:
  censors = f.read().split("\n")
censors.pop()

for line in inp:
  cur = ''
  temp = line.rstrip()
  for word in censors:
    cur = temp.replace(word, "@"*len(word))
  print(cur)
'''
# Below is just Ellie's code
# idk why the above wasn't working

censor_file = sys.argv[1]

with open(censor_file, "r") as f:
    censor_words = [w.strip() for w in f]

text = sys.stdin.read()

for w in censor_words:
    text = text.replace(w, "@"*len(w))
print(text.rstrip())


