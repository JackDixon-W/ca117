#!/usr/bin/env python3

import sys

# Grab the final answer and store it as 'final'
# Shave the last 2 lines off of 'logs' because it's no longer important
logs = sys.stdin.readlines()
final = int(logs[len(logs) - 2].rstrip())
logs = logs[:len(logs) - 2]

# 'trust' is my checker variable
# I check it at the end because it can only be set to False throughout
trust = True

# range(start, end, step) has 3 parameters
# start = starting value, defaults to 0
# end = ending value (IS NOT INCLUDED)
# Eg. setting 12 to the end value means it will run up to 11 and 
# then stop when this finishes
# step = the amount it increases by each loop, defaults to 1
for linenum in range(0, len(logs), 2):
  # temp is the line after my 'current line'
  # So this should be 'higher' or 'lower'
  temp = logs[linenum + 1].rstrip()
  if temp == "higher":
    if int(logs[linenum]) > final:
      trust = False
  elif temp == "lower":
    if int(logs[linenum]) < final:
      trust = False
  
  # This was just for error checking, it should never print
  else:
    print("ERROR")

# At the end, we check if trust is still true
if trust is True:
  print("Bert can be trusted")
else:
  print("Bert is not to be trusted")

