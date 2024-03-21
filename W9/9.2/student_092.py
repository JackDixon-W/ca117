class Student(object):
  def __init__(self, name, sid, mods):
    self.name = name
    self.sid = sid
    self.mods = mods

  def getAvg(self):
    total = 0
    length = 0
    for mod in self.mods:
      total += int(mod[1])
      length += 1
    return round(total / length)

  def getMods(self):
    out = []
    for mod in self.mods:
      out.append(mod[0])
    out.sort()
    return ', '.join(out)

  def __str__(self):
    out = []
    out.append(f'Name: {self.name}')
    out.append(f'ID: {self.sid}')
    mods = self.getMods()
    out.append(f'Modules: {mods}')
    avg = self.getAvg()
    out.append(f'Average mark: {avg}')
    return '\n'.join(out)

def main():

    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    print(s1)
    print(s2)

if __name__ == '__main__':
    main()
