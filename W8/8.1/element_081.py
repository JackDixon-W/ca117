class Element(object):
  def set_attributes(self, number, name, symbol, bp):
    self.number = number
    self.name = name
    self.symbol = symbol
    self.bp = bp

  def print_attributes(self):
    print(f'Number: {self.number}')
    print(f'Name: {self.name}')
    print(f'Symbol: {self.symbol}')
    print(f'Boiling point: {self.bp} K')

def main():

    e1 = Element()
    e2 = Element()
    e3 = Element()
    e4 = Element()
    e5 = Element()

    e1.set_attributes(1, 'Hydrogen', 'H', 20.3)
    e1.print_attributes()

    assert(e1.number == 1)
    assert(e1.name == 'Hydrogen')
    assert(e1.symbol == 'H')
    assert(e1.bp == 20.3)

    e2.set_attributes(3, 'Lithium', 'Li', 1615)
    e2.print_attributes()

    e3.set_attributes(11, 'Sodium', 'Na', 1156)
    e3.print_attributes()

    e4.set_attributes(12, 'Magnesium', 'Mg', 1380)
    e4.print_attributes()

    e5.set_attributes(79, 'Gold', 'Au', 3129)
    e5.print_attributes()


if __name__ == '__main__':
    main()
