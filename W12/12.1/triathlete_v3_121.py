class Triathlete(object):
  def __init__(self, name, tid, sports=None, racetime=0):
    self.name = name
    self.tid = tid
    if sports is None:
      self.sports = {}
    else:
      self.sports = sports
    self.racetime = racetime

  def __str__(self):
    out = []
    out.append(f'Name: {self.name}')
    out.append(f'ID: {self.tid}')
    out.append(f'Race time: {self.racetime}')
    return '\n'.join(out)

  def add_time(self, sport, time):
    self.sports[sport] = time
    self.racetime += int(time)

  def get_time(self, sport):
    return self.sports[sport]

  def __eq__(self, other):
    return self.racetime == other.racetime

  def __gt__(self, other):
    return self.racetime > other.racetime

def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)

if __name__ == '__main__':
    main()
