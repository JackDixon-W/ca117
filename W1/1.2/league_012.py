#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

length = 0
for line in inp:
  line = line.rstrip("\n")
  if len(line) > length:
    length = len(line)

# Total of 35 characters + CLUB (Includes whitespace between columns)
club = length - 35
print(club)

for line in inp:
  line = line.rstrip("\n")
  info = line.split()
  club_end = len(info) - 8
  club_name = " ".join(info[1:club_end])
  print(f'{info[0]:>3} {club_name:<{club}} ', end = '')
  print(f'{info[club_end + 1]:>2} {info[club_end + 2]:>3} ', end = '')
  print(f'{info[club_end + 3]:>3} {info[club_end + 4]:>3} ', end = '')
  print(f'{info[club_end + 5]:>3} {info[club_end + 6]:>3} ', end = '')
  print(f'{info[club_end + 7]:>3}')

