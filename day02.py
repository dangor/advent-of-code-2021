from test import build_test

def p1(input):
  file = open(input)
  ints = list(map(int, file.readlines()[0].split(',')))
  file.close()

  ints[1] = 12
  ints[2] = 2

  run_intcode(ints)

  print(ints[0])

def p2(input):
  file = open(input)
  ints = list(map(int, file.readlines()[0].split(',')))
  file.close()

  original = ints.copy()

  for i in range(100):
    for j in range(100):
      ints = original.copy()
      ints[1] = i
      ints[2] = j

      run_intcode(ints)

      if ints[0] == 19690720:
        print(100 * i + j)
        return
  
  raise

def run_intcode(ints):
  cur = 0
  while ints[cur] != 99:
    a = ints[ints[cur+1]]
    b = ints[ints[cur+2]]
    if ints[cur] == 1:
      value = a + b
    elif ints[cur] == 2:
      value = a * b

    ints[ints[cur+3]] = value
    cur += 4

def test():
  test_case = build_test(run_test)
  test_case("1,0,0,0,99", "2,0,0,0,99")
  test_case("2,3,0,3,99", "2,3,0,6,99")
  test_case("2,4,4,5,99,0", "2,4,4,5,99,9801")
  test_case("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")

def run_test(input):
  ints = list(map(int, input.split(',')))
  run_intcode(ints)
  return ','.join(str(x) for x in ints)