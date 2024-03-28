import sys

class BFSPaths(object):
  def __init__(self, g, s):
    self.g = g
    self.s = s
    # Once queued a vertex is marked
    # Initially none of the vertices have been marked
    self.marked = [False] * g.V
    # We need to remember how we reached each vertex
    self.parent = [-1] * g.V
    print(self.parent)
    self.bfs(s)

  def bfs(self, s):
    # we start at s
    # remember bfs is non-recursive and is queue-based
    # initialise our queue
    queue = [s]
    # mark s as having been queued so we do not queue it again
    # TODO

    # while we have vertices to visit
    # i.e. while the queue is non-empty
    # TODO while
    # Remove the vertex at the head of the queue
    # TODO
    # consider where we can go from this vertex
    # add any non-marked vertices to the queue
    # TODO
    # record how each was reached
    # TODO
    # mark it so we never queue it again
    # TODO
    pass

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
