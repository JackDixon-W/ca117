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

class Triathlon(object):
  def __init__(self):
    self.athletes = []

  def add(self, athlete):
    self.athletes.append(athlete)

  def best(self):
    best = 5000
    tmp = ''
    for athlete in self.athletes:
      if athlete.racetime < best:
        best = athlete.racetime
        tmp = str(athlete)
    return tmp

  def worst(self):
    worst = 0
    tmp = ''
    for athlete in self.athletes:
      if athlete.racetime > worst:
        worst = athlete.racetime
        tmp = str(athlete)
    return tmp

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
