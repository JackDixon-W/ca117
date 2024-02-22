def get_divisors(num):
  """
  Gives all divisors of a given num
  """
  out = []
  for i in range(1, (num // 2) + 1):
    if num % i == 0:
      out.append(i)
  out.append(num)
  return out

def get_proper_divisors(num):
  """
  Gives all proper divisors of the given number
  """
  divisors = get_divisors(num)
  divisors.remove(num)
  return divisors

def is_perfect(num):
  """
  Returns true if the given number is perfect
  ie. All its proper divisors add to equal it
  """
  proper = get_proper_divisors(num)
  total = 0
  for number in proper:
    total += number
  if total == num:
    return True
  return False

def main():
    print(get_divisors(6))
    print(get_proper_divisors(6))
    print(is_perfect(6))

    numbers = [1, 2, 3, 4, 5, 6, 28, 496, 8128, 8129]

    for n in numbers:
        print(is_perfect(n))

if __name__ == '__main__':
  main()
