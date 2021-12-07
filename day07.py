def p1(input):
  file = open(input)
  positions = list(map(int, file.readlines()[0].strip('\n').split(',')))
  file.close()

  def sum_fuel(test_position):
    fuel = list(abs(x - test_position) for x in positions)
    return sum(fuel)

  min = sum_fuel(0)

  for i in range(1, len(positions)):
    test = sum_fuel(i)
    if test < min:
      min = test
    else:
      return min

  raise "fail"

def p2(input):
  file = open(input)
  positions = list(map(int, file.readlines()[0].strip('\n').split(',')))
  file.close()

  def sum_fuel(test_position):
    sum = 0
    for x in positions:
      dist = abs(x - test_position)
      sum += (1 + dist) / 2 * dist
    return sum

  min = sum_fuel(0)

  for i in range(1, len(positions)):
    test = sum_fuel(i)
    if test < min:
      min = test
    else:
      return min

  raise "fail"
