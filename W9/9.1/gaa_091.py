class Score(object):
  def __init__(self, goals=0, points=0):
    self.goals = goals
    self.points = points

  def __str__(self):
    return f'{self.goals} goal(s) and {self.points} point(s)'

def main():

    s1 = Score()
    print(s1)

    s2 = Score(3, 12)
    assert(s2.goals == 3)
    assert(s2.points == 12)
    print(s2)

if __name__ == '__main__':
    main()
