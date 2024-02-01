#!/usr/bin/env python3

import sys

# Binary search (adapted from CA116)
def binsearch(query, sorted_list):

    '''Return True if query in sorted_list else False'''
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        #  print(f'{low} {mid} {high}')

        if sorted_list[mid].lower() < query.lower():
            # Search RHS
            low = mid + 1

        elif sorted_list[mid].lower() > query.lower():
            # Search LHS
            high = mid - 1

        else:
            # Found it
            return True

    # Not found
    return False

words = [word for word in sys.stdin.read().split()]

reversecomp = [word.strip() for word in words if len(word.strip()) >= 5 and binsearch(word.strip()[::-1], words)]
print(reversecomp)
