#!/usr/env/python3

# Obtained from https://git.pogr.cc/dcu/ca117/-/tree/main/lab-2-1

import sys

unique_words = []

def clean_word(word) -> str:
    """Returns a clean (no puncuation only alpha-num characters) string of the given word"""

    clean = ""
    
    for c in word:
        if c.isalnum():
            clean += c

    return clean

def check_for_unique(line):
    """Checks if there are any unique words in the input, and if so adds them to the unique_words list"""

    data = line.lower().split()
    for word in data:
        clean = clean_word(word)
        if clean not in unique_words and len(clean) > 0:
            unique_words.append(clean)

for line in sys.stdin:
    line = line.strip()

    check_for_unique(line)

# unique_words.sort()
print(len(unique_words))

