def p1(input):
  file = open(input)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  (horizontal, depth) = movement(directions)
  return horizontal * depth

def p2(input):
  file = open(input)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  (horizontal, depth) = movement(directions, True)
  return horizontal * depth

def movement(directions, corrected = False):
  horizontal = 0
  depth = 0
  aim = 0

  for direction in directions:
    [d, i] = direction.split()
    i = int(i)
    if d == "forward":
      horizontal += i
      if corrected:
        depth += aim * i
    elif d == "down":
      if not corrected:
        depth += i
      aim += i
    elif d == "up":
      if not corrected:
        depth -= i
      aim -= i
  
  return (horizontal, depth)
