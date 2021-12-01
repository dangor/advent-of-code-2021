import time
import day01, day02, day03, day04

p1, p2 = 'p1', 'p2'
def run(module, p, input):
  start = time.time()

  print(f"\n{module.__name__} {p}:")
  getattr(module, p)(input)

  end = time.time()
  print(f"(t={end - start})")

run(day01, p1, "inputs/day01.txt")
run(day01, p2, "inputs/day01.txt")

day02.test()
run(day02, p1, "inputs/day02.txt")
run(day02, p2, "inputs/day02.txt")

day03.test()
run(day03, p1, "inputs/day03.txt")
run(day03, p2, "inputs/day03.txt")

day04.test()
run(day04, p1, [178416, 676461])
run(day04, p2, [178416, 676461])