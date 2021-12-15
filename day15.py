from a_star import a_star

def p1(input):
  file = open(input)
  lines = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  start = (0, 0)
  goal = (len(lines) - 1, len(lines[0]) - 1)

  def neighbors(coord):
    neighbors = []
    if coord[0] < goal[0]:
      neighbors.append((coord[0] + 1, coord[1]))
    if coord[1] < goal[1]:
      neighbors.append((coord[0], coord[1] + 1))
    return neighbors

  path = a_star(lines, start, goal, neighbors)

  path.pop(0) # remove start
  risk = 0
  for coord in path:
    risk += lines[coord[0]][coord[1]]

  return risk