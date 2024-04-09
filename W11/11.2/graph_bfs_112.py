import sys

class BFSPaths(object):
  def __init__(self, g, s):
    self.g = g
    self.s = s
    self.marked = [False] * g.V
    self.parent = [-1] * g.V
    self.bfs(s)

  def bfs(self, s):
    queue = [s]
    self.marked[s] = True
    
    while queue:
      tmp = queue.pop(0)
      self.marked[tmp] = True
      for point in self.g.adj[tmp]:
        if not self.marked[point]:
          queue.append(point)
          self.parent[point] = tmp
          self.marked[point] = True

  def hasPathTo(self, c):
    return self.marked[c]

  def pathTo(self, d):
    if not self.hasPathTo(d):
      return []
    
    path = [d]
    while d != self.s:
      d = self.parent[d]
      path.append(d)
    
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

    bfs = BFSPaths(g, 4)

    print(bfs.hasPathTo(2))

    print(bfs.pathTo(2))

if __name__ == '__main__':
    main()
