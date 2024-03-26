import sys

inp = sys.stdin.read().split('\n')
highest = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for word in inp:
  last = ''
  count = 0
  for char in word:
    if char == last and char in vowels:
      count += 1
      last = ''
    else:
      last = char
  if count > highest:
    highest = count
    hWord = word

print(hWord)
