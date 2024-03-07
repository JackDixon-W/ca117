class Point(object):
  def set_attributes(self, x, y):
    self.x = x
    self.y = y

  def print_attributes(self):
    print(f'x: {self.x:.2f}')
    print(f'y: {self.y:.2f}')

  def reflect(self):
    self.x = self.x * -1
    self.y = self.y * -1

def main():
    p1 = Point()
    p2 = Point()

    p1.set_attributes(5, 5)
    p2.set_attributes(4.2, 3.8)

    p1.print_attributes()
    p2.print_attributes()

    assert(p1.x == 5)
    assert(p1.y == 5)

    p1.reflect()
    p1.print_attributes()

    assert(p1.x == -5)
    assert(p1.y == -5)

if __name__ == '__main__':
    main()
