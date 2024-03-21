class Queue(object):
  def __init__(self):
    self.l = []

  def enqueue(self, e):
    self.l.append(e)

  def dequeue(self):
    try:
      tmp = self.l[0]
      self.l.pop(0)
      return tmp
    except TypeError:
      return "Error"

  def first(self):
    try:
      return self.l[0]
    except TypeError:
      return "Error"

  def is_empty(self):
    return len(self.l) == 0

  def __len__(self):
    return len(self.l)

def main():

    q = Queue()

    print(len(q))
    q.enqueue(1)
    print(q.first())
    print(q.is_empty())
    print(q.dequeue())
    print(q.is_empty())
    try:
        print(q.dequeue())
    except IndexError:
        print('Error')
    try:
        print(q.first())
    except IndexError:
        print('Error')
    q.enqueue('cat')
    q.enqueue('dog')
    q.enqueue('fish')
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())

if __name__ == '__main__':
    main()
