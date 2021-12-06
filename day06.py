def p1(input):
  file = open(input)
  timers = list(map(int, file.readlines()[0].strip('\n').split(',')))
  file.close()

  counts = [0]*9
  for timer in timers:
    counts[timer] += 1

  for generation in range(80):
    new = counts[0]
    for i in range(len(counts) - 1):
      counts[i] = counts[i+1]
    counts[8] = new
    counts[6] += new

  return sum(counts)