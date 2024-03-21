def collatz(n):
  if n == 1:
    print(n)
    return 1
  print(n)
  if n % 2 == 0:
    collatz(n // 2)
  else:
    collatz((n*3)+1)
  

def main():
    collatz(5)

if __name__ == '__main__':
    main()
