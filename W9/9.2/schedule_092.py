class Meeting(object):
  def __init__(self, hour, minute, duration):
    self.hour = hour
    self.minute = minute
    self.duration = duration

  def __str__(self):
    return f'{self.hour:02}:{self.minute:02} ({self.duration} minutes)'

class Schedule(object):
  def __init__(self):
    self.total = 0
    self.sched = []
  
  def add(self, meet):
    self.sched.append(meet)
    self.total += 1

  def __str__(self):
    out = []
    out.append('Schedule')
    out.append('--------')
    for meet in self.sched:
      out.append(str(meet))
    out.append(f'Meetings today: {self.total}')
    out[2:3 + self.total] = sorted(out[2:3 + self.total])
    return '\n'.join(out)

def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)

if __name__ == '__main__':
    main()
