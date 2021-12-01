from test import build_test

def p1(input):
  file = open(input)
  depths = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  output = count_window_increases(depths, 1)
  print(output)

def p2(input):
  file = open(input)
  depths = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  output = count_window_increases(depths, 3)
  print(output)

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

def test():
  test_case = build_test(p1_test)
  test_case([199,200,208,210,200,207,240,269,260,263], 7)

  test_case = build_test(p2_test)
  test_case([199,200,208,210,200,207,240,269,260,263], 5)

def p1_test(input):
  return count_window_increases(input, 1)

def p2_test(input):
  return count_window_increases(input, 3)