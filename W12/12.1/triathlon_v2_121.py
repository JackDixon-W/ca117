class Triathlete(object):
  def __init__(self, name, tid):
    self.name = name
    self.tid = tid

  def __str__(self):
    out = []
    out.append(f'Name: {self.name}')
    out.append(f'ID: {self.tid}')
    return '\n'.join(out)

class Triathlon(object):
  def __init__(self, athletes=None):
    if athletes is None:
      self.athletes = []
    else:
      self.athletes = athletes

  def add(self, athlete):
    self.athletes.append(athlete)

  def remove(self, tid):
    self.athletes.remove(self.lookup(tid))

  def lookup(self, tid):
    for athlete in self.athletes:
      if athlete.tid == tid:
        return athlete
    return None

  def __str__(self):
    out = []
    for athlete in self.athletes:
      out.append(str(athlete))
    out.sort()
    return '\n'.join(out)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
