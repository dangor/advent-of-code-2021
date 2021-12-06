def p1(input):
  file = open(input)
  timers = list(map(int, file.readlines()[0].strip('\n').split(',')))
  file.close()

  return spawn_fish(timers, 80)

def p2(input):
  file = open(input)
  timers = list(map(int, file.readlines()[0].strip('\n').split(',')))
  file.close()

  return spawn_fish(timers, 256)

def spawn_fish(timers, generations):
  counts = [0]*9
  for timer in timers:
    counts[timer] += 1

  for generation in range(generations):
    new = counts[0]
    for i in range(len(counts) - 1):
      counts[i] = counts[i+1]
    counts[8] = new
    counts[6] += new

  return sum(counts)
