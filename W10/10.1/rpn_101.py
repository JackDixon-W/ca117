import sys
from math import sqrt

class Stack(object):
  def __init__(self):
      self.l = []

  def push(self, e):
      self.l.append(e)

  def pop(self):
      return self.l.pop()

  def top(self):
      return self.l[-1]

  def is_empty(self):
      return len(self.l) == 0

  def __len__(self):
      return len(self.l)

def calculator(line):

  binops = {'+': float.__add__,
            '-': float.__sub__,
            '*': float.__mul__,
            '/': float.__truediv__}

  uniops = {'n': float.__neg__, 'r': sqrt}

  st = Stack()
  line = line.split(' ')
  for char in line:
    if char.isdigit() or '.' in char:
      st.push(float(char))
    elif char in uniops:
      num = st.pop()
      """
      print(f'Num={num}')
      print('Uniops=', uniops[char](num))
      """
      st.push(uniops[char](num))
    elif char in binops:
      num1 = st.pop()
      num2 = st.pop()
      """
      print(f'Num1={num1} and Num2={num2}')
      print('Binops=', binops[char](num2, num1))
      """
      st.push(binops[char](num1, num2))
  if len(st) == 1:
    return st.pop()
  else:
    raise IndexError

tests = ['5',
'8.5 2 /',
'2 3 +',
'2 3 r +',
'1 2 3 * +',
'5 2 n *',
'1 2 3 + -',
'2 1 2 3 + - *',
'2 1 2 3 + - * n',
'2 1 2 3 + - * n r',
'6 +',
'9 r']

def main():

    for test in tests:
        try:
            a = calculator(test.strip())
            print('{:.2f}'.format(a))
            print('----------------------')
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()
