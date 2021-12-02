import time
import day01, day02

p1, p2 = 'p1', 'p2'
def run(module, p):
  start = time.time()

  print(f"\n{module.__name__} {p}:")
  getattr(module, p)(f"inputs/{module.__name__}.txt")

  end = time.time()
  print(f"(t={end - start})")

day01.test()
run(day01, p1)
run(day01, p2)

day02.test()
run(day02, p1)