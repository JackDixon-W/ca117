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

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
