#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

fletters = [word.strip() for word in inp if len(word.strip()) == 17]
print(f'Words containing 17 letters: {fletters}')

sletters = [word.strip() for word in inp if len(word.strip()) >= 18]
print(f'Words containing 18+ letters: {sletters}')

a = [word.strip() for word in inp if word.count('a') + word.count('A') == 4]
print(f"Words with 4 a's: {a}")

q = [word.strip() for word in inp if word.count('q') + word.count('Q') >= 2]
print(f"Words with 2+ q's: {q}")

cie = [word.strip() for word in inp if "cie" in word]
print(f'Words containing cie: {cie}')

anagrams = [word.strip() for word in inp if sorted(word.strip().lower()) == sorted("angle") and word.strip() != "angle"]
print(f'Anagrams of angle: {anagrams}')

