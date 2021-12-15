def p1(input):
  file = open(input)
  lines = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  global min_risk
  min_risk = 10*100

  traverse(lines)

  return min_risk - lines[0][0]

def traverse(lines, i = 0, j = 0, current = 0):
  global min_risk

  new_current = current + lines[i][j]
  if new_current >= min_risk:
    # short circuit
    return min_risk

  if i == len(lines) - 1 and j == len(lines[0]) - 1:
    # at the end
    if new_current < min_risk:
      min_risk = new_current
    return

  if i < len(lines) - 1:
    # go right
    traverse(lines, i + 1, j, new_current)

  if j < len(lines[0]) - 1:
    # go down
    traverse(lines, i, j + 1, new_current)

  return
