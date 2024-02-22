import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
  """
  Returns True if two circles overlap
  Find the distance between the two circles
  Compare it to the sum of radii
  If equal, return true
  """
  d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
  if d < (r2 + r1):
    return True
  return False

def main():
    print(overlap())
    print(overlap(10))
    print(overlap(10,10))
    print(overlap(10,10,10))
    print(overlap(10,0,10))
    print(overlap(10,0,1,8,0,1))
    print(overlap(10,0,1,8,0,2))


if __name__ == '__main__':
    main()
