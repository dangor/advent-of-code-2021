from math import ceil

class Node(object):
  def __init__(self, left = None, right = None, parent = None):
    self.left = left
    self.right = right
    self.parent = parent
    self.neighbor_left = None
    self.neighbor_right = None

  def __str__(self):
    return f"[{self.left},{self.right}]"

  def explode(self, depth = 0):
    if type(self.left) == Node and self.left.explode(depth + 1):
      return True
    elif type(self.right) == Node and self.right.explode(depth + 1):
      return True
    elif depth >= 4:
      current = self
      while current and current.neighbor_left is None:
        current = current.parent
      if current and type(current.neighbor_left) != Node:
        current = current.parent
        print(f"exploding left {self.left} -> {current.left}")
        current.left += self.left
      elif current:
        current = current.neighbor_left
        while current and type(current.right) == Node:
          current = current.right
        if current:
          print(f"exploding left {self.left} -> {current.right}")
          current.right += self.left

      current = self
      while current and current.neighbor_right is None:
        current = current.parent
      if current and type(current.neighbor_right) != Node:
        current = current.parent
        print(f"exploding right {self.right} -> {current.right}")
        current.right += self.right
      elif current:
        current = current.neighbor_right
        while current and type(current.left) == Node:
          current = current.left
        if current:
          print(f"exploding right {self.right} -> {current.left}")
          current.left += self.right
      
      if self.parent.left == self:
        self.parent.left = 0
        if type(self.parent.right) == Node:
          self.parent.right.neighbor_left = 0

      if self.parent.right == self:
        self.parent.right = 0
        if type(self.parent.left) == Node:
          self.parent.left.neighbor_right = 0

      return True

    return False

  def split(self):
    if type(self.left) == Node and self.left.split():
      return True
    elif type(self.right) == Node and self.right.split():
      return True
    elif type(self.left) != Node and self.left >= 10:
      print(f"splitting {self.left}")
      self.left = Node(self.left // 2, ceil(self.left / 2), self)
      self.left.neighbor_right = self.right
      if type(self.right) == Node:
        self.right.neighbor_left = self.left
      return True
    elif type(self.right) != Node and self.right >= 10:
      print(f"splitting {self.right}")
      self.right = Node(self.right // 2, ceil(self.right / 2), self)
      self.right.neighbor_left = self.left
      if type(self.left) == Node:
        self.left.neighbor_right = self.right
      return True

    return False
      
def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  current = convert_to_btree(eval(lines.pop(0)))
  while lines:
    current = Node(current, convert_to_btree(eval(lines.pop(0))))
    print(current)
    current.left.parent = current
    current.right.parent = current
    current.left.neighbor_right = current.right
    current.right.neighbor_left = current.left
    reduce_snail(current)
    break

  return magnitude(current)

def convert_to_btree(snail, parent = None):
  if type(snail) != list:
    return snail
  
  new = Node(parent = parent)
  new.left = convert_to_btree(snail[0], new)
  new.right = convert_to_btree(snail[1], new)
  if type(new.left) == Node:
    new.left.neighbor_right = new.right
  if type(new.right) == Node:
    new.right.neighbor_left = new.left
  return new

def reduce_snail(snail):
  while True:
    while True:
      exploded = snail.explode()
      if not exploded:
        break
      else:
        print(snail)

    did_split = snail.split()
    if not did_split:
      break
    else:
      print(snail)

  return snail

def magnitude(snail):
  if type(snail) != Node:
    return snail

  return 3 * magnitude(snail.left) + 2 * magnitude(snail.right)