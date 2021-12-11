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