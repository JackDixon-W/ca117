def power(n1, n2):
  if n2 == 0:
    return 1
  return n1 * power(n1, n2-1)

def main():
    print(power(2,3))
    print(power(4,4))
    print(power(2,32))
    print(power(10,3))
    print(power(8,0))

if __name__ == '__main__':
    main()
