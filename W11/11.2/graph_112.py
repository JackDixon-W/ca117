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

def main():

    with open('graph_input_00_112.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    for v in range(g.V):
        print('Vertex {} connects to {}'.format(v, g.adj[v]))
    for v in range(V):
        print('Degree of vertex {} is {}'.format(v, g.degree(v)))
    print('Maximum degree is {}'.format(g.maxDegree()))
    print('Average degree is {:.2f}'.format(g.avgDegree()))

if __name__ == '__main__':
    main()
