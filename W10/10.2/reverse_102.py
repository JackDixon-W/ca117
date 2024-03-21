def reverse(s):
  if not s:
    return []
  else:
    return [s[-1]] + reverse(s[:-1])

def main():
    print(reverse([1,2,3]))
    print(reverse([3,4,5,6]))
    print(reverse([1,2]))

def test():
    print(reverse('hello'))
    print(reverse('testing'))
    print(reverse('rotator'))

if __name__ == '__main__':
    main()
