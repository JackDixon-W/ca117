#!/usr/bin/env python3

import sys

class CashRegister(object):
  def __init__(self, items=[]):
    self.items = items
    self.count = len(items)
    self.total = 0

  def add_item(self, item):
    self.items.append(item)
    self.total += item
    self.count += 1

  def clear(self):
    self.items = []
    self.count = 0
    self.total = 0

  def __str__(self):
    return f'Items: {self.count}\nTotal: {self.total:.2f}'

def main():

    cr = CashRegister()
    print(cr)

    cr.add_item(3.28)
    assert(cr.total == 3.28)
    assert(cr.count == 1)

    cr.add_item(12.92)
    print(cr)

    cr.clear()

    cr.add_item(9.1)
    print(cr)

if __name__ == '__main__':
    main()
