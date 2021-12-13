def p1(input):
  file = open(input)
  (coords, folds) = parse(file)
  file.close()

  fold = folds[0]
  if fold[0] == 'x':
    coords = fold_x(coords, fold[1])
  else:
    coords = fold_y(coords, fold[1])

  return len(coords)
    
def fold_x(coords, x):
  copy = list(coords)
  for coord in copy:
    if coord[0] > x:
      new_coord = (x - (coord[0] - x), coord[1])
      coords.add(new_coord)
      coords.remove(coord)

  return coords

def fold_y(coords, y):
  copy = list(coords)
  for coord in copy:
    if coord[1] > y:
      new_coord = (coord[0], y - (coord[1] - y))
      coords.add(new_coord)
      coords.remove(coord)

  return coords

def parse(file):
  coords = set()
  folds = []

  lines = list(x.strip('\n') for x in file.readlines())

  while(True):
    line = lines.pop(0)
    if line == '':
      break

    coords.add(tuple(map(int, line.split(','))))

  for line in lines:
    parts = line.split('=')
    folds.append((parts[0][-1], int(parts[1])))

  return (coords, folds)