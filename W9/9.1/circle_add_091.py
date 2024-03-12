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

class Circle(object):
  def __init__(self, centre=None, radius=1):
    if centre is not None:
      self.centre = centre
    else:
      self.centre = Point(0, 0)
    self.radius = radius

  def midpoint(self, other):
    finX = (self.centre.x + other.centre.x) / 2
    finY = (self.centre.y + other.centre.y) / 2
    return Point(finX, finY)

  def __str__(self):
    return f'Centre: {self.centre}\nRadius: {self.radius}'

  def __add__(self, other):
    newCentre = self.midpoint(other)
    newRadius = self.radius + other.radius
    return Circle(newCentre, newRadius)

def main():
    p1 = Point()
    p2 = Point(4, 6)

    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)

    c3 = c1 + c2
    assert(isinstance(c3, Circle))
    print(c3)

if __name__ == '__main__':
    main()
