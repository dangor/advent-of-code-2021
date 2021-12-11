def p1(input):
  file = open(input)
  lines = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  risk = 0

  for i in range(len(lines)):
    for j in range(len(lines[0])):
      if is_local_min(lines, i, j):
        risk += lines[i][j] + 1

  return risk

def p2(input):
  file = open(input)
  lines = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  sizes = []

  for i in range(len(lines)):
    for j in range(len(lines[0])):
      if is_local_min(lines, i, j):
        sizes.append(measure_basin(lines, i, j))

  sizes.sort()

  return sizes[-1] * sizes[-2] * sizes[-3]

def is_local_min(lines, i, j):
  value = lines[i][j]
  offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for o in offsets:
    a = i + o[0]
    b = j + o[1]
    if a not in range(len(lines)) or b not in range(len(lines[0])):
      continue
    if lines[a][b] <= value:
      return False
  return True

def measure_basin(lines, i, j, visited = set()):
  visited.add((i, j))
  offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  total = 1
  for o in offsets:
    a = i + o[0]
    b = j + o[1]
    if a not in range(len(lines)) or b not in range(len(lines[0])):
      continue
    if lines[a][b] == 9:
      continue
    if (a, b) in visited:
      continue
    total += measure_basin(lines, a, b, visited)

  return total