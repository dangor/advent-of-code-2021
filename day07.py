def p1(input):
  file = open(input)
  positions = list(map(int, file.readlines()[0].strip('\n').split(',')))
  file.close()

  min = sum_fuel(positions, 0)

  for i in range(1, len(positions)):
    test = sum_fuel(positions, i)
    if test < min:
      min = test
    else:
      return min

  raise "fail"

def sum_fuel(positions, test_position):
  fuel = list(abs(x - test_position) for x in positions)
  return sum(fuel)