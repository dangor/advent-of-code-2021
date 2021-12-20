from math import ceil

class Node(object):
  def __init__(self, left = None, right = None, parent = None):
    self.left = left
    self.right = right
    self.set_left(left)
    self.set_right(right)
    self.parent = parent
    self.neighbor_left = None
    self.neighbor_right = None

  def __str__(self):
    return f"[{self.left},{self.right}]"

  def set_right(self, right):
    self.right = right
    if type(self.left) == Node:
      self.left.neighbor_right = right
    if type(right) == Node:
      self.right.neighbor_left = self.left
      self.right.parent = self

  def set_left(self, left):
    self.left = left
    if type(self.right) == Node:
      self.right.neighbor_left = left
    if type(left) == Node:
      self.left.neighbor_right = self.right
      self.left.parent = self

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
        #print(f"exploding left {self.left} -> {current.left}")
        current.set_left(current.left + self.left)
      elif current:
        current = current.neighbor_left
        while current and type(current.right) == Node:
          current = current.right
        if current:
          #print(f"exploding left {self.left} -> {current.right}")
          current.set_right(current.right + self.left)

      current = self
      while current and current.neighbor_right is None:
        current = current.parent
      if current and type(current.neighbor_right) != Node:
        current = current.parent
        #print(f"exploding right {self.right} -> {current.right}")
        current.set_right(current.right + self.right)
      elif current:
        current = current.neighbor_right
        while current and type(current.left) == Node:
          current = current.left
        if current:
          #print(f"exploding right {self.right} -> {current.left}")
          current.set_left(current.left + self.right)
      
      if self.parent.left == self:
        self.parent.set_left(0)

      if self.parent.right == self:
        self.parent.set_right(0)

      return True

    return False

  def split(self):
    if type(self.left) == Node and self.left.split():
      return True
    elif type(self.left) != Node and self.left >= 10:
      #print(f"splitting {self.left}")
      self.set_left(Node(self.left // 2, ceil(self.left / 2), self))
      return True
    elif type(self.right) == Node and self.right.split():
      return True
    elif type(self.right) != Node and self.right >= 10:
      #print(f"splitting {self.right}")
      self.set_right(Node(self.right // 2, ceil(self.right / 2), self))
      return True

    return False
      
def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  current = convert_to_btree(eval(lines.pop(0)))
  while lines:
    current = Node(current, convert_to_btree(eval(lines.pop(0))))
    #print(current)
    reduce_snail(current)

  return magnitude(current)

def convert_to_btree(snail, parent = None):
  if type(snail) != list:
    return snail
  
  new = Node(parent = parent)
  new.set_left(convert_to_btree(snail[0], new))
  new.set_right(convert_to_btree(snail[1], new))
  return new

def reduce_snail(snail):
  while True:
    while True:
      exploded = snail.explode()
      if not exploded:
        break

    did_split = snail.split()
    if not did_split:
      break

  return snail

def magnitude(snail):
  if type(snail) != Node:
    return snail

  return 3 * magnitude(snail.left) + 2 * magnitude(snail.right)