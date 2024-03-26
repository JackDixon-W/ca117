#!/usr/bin/env python3
from math import sqrt

class Stack(object):
    def __init__(self):
        self.l = []

    def push(self, el):
        self.l.append(el)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
    
    def __str__(self):
        return str(self.l)

binops = {"+": float.__add__,
          "-": float.__sub__,
          "*": float.__mul__,
          "/": float.__truediv__}
uniops = {"n":float.__neg__,
          "r": sqrt}

operators = list(binops.keys()) + list(uniops.keys())

"""
Examples:

# To add 3 and 5 we can do something like this...
print(binops['+'](3.0, 5.0))

# To calcualte the square root of 9 we can do something like this...
print(uniops['r'](9.0))
"""

def calculator(line):
    s = Stack()

    line = line.split()
    for i in line:
        if i not in operators:
            # is a number
            n = float(i)
            s.push(n)
        else:
            # is an operator
            if i in binops:
                # pop last 2 in stack
                num_2 = s.pop()
                num_1 = s.pop()
                calculated = binops[i](num_1, num_2)
                s.push(calculated)
            else:
                # pop last 1 in stack
                num = s.pop()
                calculated = uniops[i](num)
                s.push(calculated)
        
    final = s.pop()
    if not s.is_empty():
        raise IndexError

    return final

    print("line:", line)
    return 0
