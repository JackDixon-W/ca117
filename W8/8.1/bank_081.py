class BankAccount(object):
  def set_attributes(self, name, number, balance):
    self.name = name
    self.number = number
    self.balance = balance

  def print_attributes(self):
    print(f'Name: {self.name}')
    print(f'Account number: {self.number}')
    print(f'Balance: {self.balance:.2f}')

  def deposit(self, depositVal):
    self.balance += depositVal

def main():

    b1 = BankAccount()
    b1.set_attributes('Jim', 12343111, 300)

    assert(b1.name == 'Jim')
    assert(b1.number == 12343111)
    assert(b1.balance == 300)

    b1.print_attributes()
    b1.deposit(100)
    b1.print_attributes()

    assert(b1.balance == 400)


if __name__ == '__main__':
    main()
