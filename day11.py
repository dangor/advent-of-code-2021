def p1(input):
  file = open(input)
  current_gen = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  total = 0

  for i in range(100):
    (flashes, next_gen) = step(current_gen)
    current_gen = next_gen
    total += flashes

  return total

def step(gen):
  for i in range(len(gen)):
    for j in range(len(gen)):
      gen[i][j] += 1

  flashed = True
  while(flashed):
    flashed = False
    for i in range(len(gen)):
      for j in range(len(gen[0])):
        if gen[i][j] > 9:
          flashed = True
          gen[i][j] = 0
          inc_neighbors(gen, i, j)
  
  count = 0

  for i in range(len(gen)):
    count += gen[i].count(0)

  return (count, gen)
        
def inc_neighbors(gen, i, j):
  offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for o in offsets:
    a = i + o[0]
    b = j + o[1]
    if a not in range(len(gen)) or b not in range(len(gen)):
      continue
    if gen[a][b] == 0:
      continue
    gen[a][b] += 1
