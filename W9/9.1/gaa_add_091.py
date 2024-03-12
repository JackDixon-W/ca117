class Score(object):
  def __init__(self, goals=0, points=0):
    self.goals = goals
    self.points = points

  def __str__(self):
    return f'{self.goals} goal(s) and {self.points} point(s)'

  def finalScore(self):
    return self.goals*3 + self.points

  def __add__(self, other):
    total_goals = self.goals + other.goals
    total_points = self.points + other.points
    return Score(total_goals, total_points)

  def __iadd__(self, other):
    self.goals += other.goals
    self.points += other.points
    return self

  def __eq__(self, other):
    return self.finalScore() == other.finalScore()

  def __ge__(self, other):
    return self.finalScore() >= other.finalScore()

  def __gt__(self, other):
    return self.finalScore() > other.finalScore()

def main():

    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(1, 1)

    s5 = s3 + s4
    print(s5)
    assert(isinstance(s5, Score))
    assert(s5 is not s3)
    assert(s5 is not s4)

    before = s2
    s2 += s4
    print(s2)
    assert(isinstance(s2, Score))
    assert(s2 is before)
    assert(s2 is not s4)

if __name__ == '__main__':
    main()
