#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

length = 0
for line in inp:
  line = line.rstrip("\n")
  info = line.split()
  club_end = len(info) - 8
  club_name = " ".join(info[1:club_end])
  if len(club_name) > length:
    length = len(club_name)

temp = "CLUB"
print(f'POS {temp:<{length}} ', end = '')
print(f' P   W   D   L  GF  GA  GD PTS')

for line in inp:
  line = line.rstrip("\n")
  info = line.split()
  club_end = len(info) - 8
  club_name = " ".join(info[1:club_end])
  print(f'{info[0]:>3} {club_name:<{length}} ', end = '')
  print(f'{info[club_end]:>2} {info[club_end + 1]:>3} ', end = '')
  print(f'{info[club_end + 2]:>3} {info[club_end + 3]:>3} ', end = '')
  print(f'{info[club_end + 4]:>3} {info[club_end + 5]:>3} ', end = '')
  print(f'{info[club_end + 6]:>3} {info[club_end + 7]:>3}')

