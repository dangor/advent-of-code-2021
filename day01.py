def p1(input):
  file = open(input)
  depths = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  return count_window_increases(depths, 1)

def p2(input):
  file = open(input)
  depths = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  return count_window_increases(depths, 3)

def count_window_increases(depths, window):
  increases = 0
  
  for i in range(len(depths)):
    if i < window:
      continue

    if window_sum(depths, i, window) > window_sum(depths, i - 1, window):
      increases += 1

  return increases

def window_sum(depths, i, size):
  sum = 0
  for j in range(size):
    sum += depths[i - j]
  return sum