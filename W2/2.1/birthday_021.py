#!/usr/bin/env python3

import sys
import calendar

poem = "Monday's child is fair of face.Tuesday's child is full of grace.Wednesday's child is full of woe.Thursday's child has far to go.Friday's child is loving and giving.Saturday's child works hard for a living.Sunday's child is fair and wise and good in every way."

poem = poem.split(".")
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for line in sys.stdin:
  line = line.rstrip().split()
  day = calendar.weekday(int(line[2]), int(line[1]), int(line[0]))
  print(f'You were born on a {day_list[day]} and {poem[day]}.')

