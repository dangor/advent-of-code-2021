from test import build_test

def p1(input):
  file = open(input)
  depths = list(int(x.strip('\n')) for x in file.readlines())
  file.close()

  output = count_increases(depths)
  print(output)

def count_increases(depths):
  increases = 0

  for i in range(len(depths)):
    if i == 0:
      continue

    if depths[i] > depths[i - 1]:
      increases += 1

  return increases

def test():
  test_case = build_test(count_increases)
  test_case([199,200,208,210,200,207,240,269,260,263], 7)
