import sys

class DFSPaths(object):
  def __init__(self, g, s):
    self.g = g
    self.s = s
    self.marked = [False] * g.V
    self.parent = [-1] * g.V
    self.dfs(s)

  def dfs(self, s):
    self.marked[s] = True

    for w in self.g.adj[s]:
      if not self.marked[w]:
        self.parent[w] = s
        self.dfs(w)

  def hasPathTo(self, v):
    return self.marked[v]

  def pathTo(self, v):
    if not self.hasPathTo(v):
      return []

    path = [v]
    while v != self.s:
      v = self.parent[v]
      path.append(v)

    return path[::-1]

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

    dfs = DFSPaths(g, 4)

    print(dfs.hasPathTo(2))

    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()
