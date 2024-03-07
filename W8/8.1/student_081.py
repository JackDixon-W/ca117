class Student(object):
  def set_attributes(self, sid, name, modlist):
    self.sid = sid
    self.name = name
    self.modlist = modlist

  def print_attributes(self):
    print(f'ID: {self.sid}')
    print(f'Name: {self.name}')
    printlist = ', '.join(self.modlist)
    print(f'Modules: {printlist}')

  def add_module(self, newModule):
    self.modlist.append(newModule)

  def del_module(self, delModule):
    self.modlist.remove(delModule)

def main():

    s1 = Student()

    s1.set_attributes(15234654, 'Jimmy Murphy', ['CA116'])
    s1.print_attributes()

    assert(s1.name == 'Jimmy Murphy')
    assert(s1.sid == 15234654)
    assert(s1.modlist == ['CA116'])

    s1.add_module('CA117')
    s1.print_attributes()

    s1.add_module('CA100')
    s1.del_module('CA116')
    s1.print_attributes()

    assert(s1.modlist == ['CA117', 'CA100'])

if __name__ == '__main__':
    main()
