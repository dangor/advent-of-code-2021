def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()
  return count_revisited(lines)

def p2(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()
  return count_revisited(lines, True)

def count_revisited(lines, diagonals = False):
  seen = set()
  revisited = set()

  def process_coord(coord):
    if coord in seen:
      revisited.add(coord)
    else:
      seen.add(coord)

  for line in lines:
    components = line.split()
    coord1 = tuple(map(int, components[0].split(',')))
    coord2 = tuple(map(int, components[2].split(',')))

    if coord1[0] == coord2[0]:
      y = [coord1[1], coord2[1]]
      y.sort()
      for i in range(y[1] - y[0] + 1):
        coord = (coord1[0], y[0] + i)
        process_coord(coord)
    elif coord1[1] == coord2[1]:
      x = [coord1[0], coord2[0]]
      x.sort()
      for i in range(x[1] - x[0] + 1):
        coord = (x[0] + i, coord1[1])
        process_coord(coord)
    elif diagonals:
      x = [coord1[0], coord2[0]]
      x.sort()
      xrange = list(range(x[0], x[1] + 1)) # is there a python alternative to range?
      if coord1[0] > coord2[0]:
        xrange.reverse()
      y = [coord1[1], coord2[1]]
      y.sort()
      yrange = list(range(y[0], y[1] + 1))
      if coord1[1] > coord2[1]:
        yrange.reverse()

      assert(len(xrange) == len(yrange)) # 45 degrees

      for i in range(len(xrange)):
        coord = (xrange[i], yrange[i])
        process_coord(coord)
  
  return len(revisited)