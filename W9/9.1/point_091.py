class Point(object):
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def midpoint(self, other):
    finX = (self.x + other.x) / 2
    finY = (self.y + other.y) / 2
    return Point(finX, finY)

  def __str__(self):
    return f'({self.x:.1f}, {self.y:.1f})'

def main():
    p1 = Point(2, 3)
    p2 = Point(4, 6)

    p3 = p1.midpoint(p2)

    print(p1)
    print(p2)
    print(p3)

    assert(isinstance(p3, Point))

if __name__ == '__main__':
    main()
