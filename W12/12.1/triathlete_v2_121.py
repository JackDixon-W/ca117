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

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
