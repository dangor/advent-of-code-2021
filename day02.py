from test import build_test

def p1(input):
  file = open(input)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  (horizontal, depth) = movement(directions)
  print(horizontal * depth)

def movement(directions):
  horizontal = 0
  depth = 0

  for direction in directions:
    [d, i] = direction.split()
    i = int(i)
    if d == "forward":
      horizontal += i
    elif d == "down":
      depth += i
    elif d == "up":
      depth -= i
  
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
