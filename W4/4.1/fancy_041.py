#!/usr/bin/env python3

import sys

file = sys.argv[1]
with open(file, 'r') as f:
  filelist = f.read().split("\n")
filelist.pop()

lib = {}
for line in filelist:
  cur = line.split()
  lib[cur[0]] = (cur[1], cur[2])

inp = sys.stdin.readlines()

for name in inp:
  try:
    name = name.rstrip()
    print(f'Name: {name}')
    print(f'Phone: {lib[name][0]}')
    print(f'Email: {lib[name][1]}')
  except KeyError:
    print('No such contact')
