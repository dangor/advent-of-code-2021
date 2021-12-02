from test import build_test

def p1(input):
  file = open(input)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  (horizontal, depth) = movement(directions)
  print(horizontal * depth)

def p2(input):
  file = open(input)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  (horizontal, depth) = movement(directions, True)
  print(horizontal * depth)

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

def test():
  test_case = build_test(movement)
  test_case([
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
  ], (15, 10))

  test_case = build_test(p2_test)
  test_case([
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
  ], (15, 60))

def p2_test(input):
  return movement(input, True)