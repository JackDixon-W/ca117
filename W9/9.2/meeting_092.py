class Meeting(object):
    def __init__(self, hour, minute, duration):
      self.hour = hour
      self.minute = minute
      self.duration = duration

    def __str__(self):
      return f'{self.hour:02}:{self.minute:02} ({self.duration} minutes)'

def main():

    m = Meeting(9, 5, 30)

    assert(m.hour == 9)
    assert(m.minute == 5)
    assert(m.duration == 30)

    print(m)

if __name__ == '__main__':
    main()
