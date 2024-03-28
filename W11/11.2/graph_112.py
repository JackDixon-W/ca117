import sys

class Graph(object):

  def __init__(self, V):
    self.V = V
    self.adj = {}
    for v in range(self.V):
      self.adj[v] = list() # []

  def addEdge(self, v, w):
    self.adj[v].append(w)
    self.adj[w].append(v)

  def degree(self, v):
    return len(self.adj[v])

  def avgDegree(self):
    total = 0
    for v in range(self.V):
      total += self.degree(v)
    return total / self.V

  def maxDegree(self):
    highest = 0
    for v in range(self.V):
      if self.degree(v) > highest:
        highest = self.degree(v)
    return highest

