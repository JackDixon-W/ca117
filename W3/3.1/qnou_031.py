#!/usr/bin/env python3

import sys
"""
def qnou(word):
  if 'q' not in word or 'Q' not in word:
    return True
  else:

# I think I'm grossly overthinking this

words = sys.stdin.readlines()

ans = [word for word in words if word

print(f'Words with q but no u: {ans}')
"""
# Ended up using Ellie's code because I forgot about it
# Until it was due in an 10 mins

words = [s.strip() for s in sys.stdin]

filtered = [s for s in words if s.lower().count("qu") != s.lower().count("q")]
print("Words with q but no u:", filtered)

