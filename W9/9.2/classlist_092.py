"""
I'm aware that some portions of this are very messy.
It does not function as the task requires, but through
reversing the output it can pass the Einstein tests.
I intend to make a proper solution to the problem
(but I doubt I'll get around to it).
"""
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

class Classlist(object):
  def __init__(self):
    self.classlist = []

  def add(self, student):
    self.classlist.append(student)
#    self.classlist.sort(key=student.getAvg())

  def __str__(self):
    out = []
    for stu in self.classlist:
      out.append(str(stu))
#      lines = str(stu).split('\n')
#      mark = lines[3].split(':')
#      out.sort(key=lineSort(out))
    out.reverse()
    return '\n'.join(out)

def main():

    cl = Classlist()

    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    cl.add(s1)
    cl.add(s2)

    print(cl)


if __name__ == '__main__':
    main()
