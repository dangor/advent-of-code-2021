from functools import reduce

def p1(input):
  file = open(input)
  masses = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  sum = reduce(lambda x, y: x + y // 3 - 2, masses, 0)

  print(sum)

def p2(input):
  file = open(input)
  masses = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  sum = 0
  for mass in masses:
    sum += recurse_fuel(mass)

  print(sum)

def recurse_fuel(mass):
  fuel = mass // 3 - 2
  if fuel <= 0:
    return 0

  return fuel + recurse_fuel(fuel)
