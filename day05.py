def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  seen = set()
  revisited = set()

  for line in lines:
    components = line.split()
    coord1 = tuple(map(int, components[0].split(',')))
    coord2 = tuple(map(int, components[2].split(',')))

    if coord1[0] == coord2[0]:
      y = [coord1[1], coord2[1]]
      y.sort()
      for i in range(y[1] - y[0] + 1):
        coord = (coord1[0], y[0] + i)
        if coord in seen:
          revisited.add(coord)
        else:
          seen.add(coord)
    elif coord1[1] == coord2[1]:
      x = [coord1[0], coord2[0]]
      x.sort()
      for i in range(x[1] - x[0] + 1):
        coord = (x[0] + i, coord1[1])
        if coord in seen:
          revisited.add(coord)
        else:
          seen.add(coord)
          
  return len(revisited)