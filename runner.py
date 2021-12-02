import time

def run(module, p, expected):
  print(f"\n{module.__name__} {p}:")

  # test input
  actual = getattr(module, p)(f"inputs/{module.__name__}test.txt")
  assert actual == expected, f"Input: {input}\nActual: {actual}, Expected: {expected}"

  start = time.time()

  # real input
  output = getattr(module, p)(f"inputs/{module.__name__}.txt")
  print(output)

  end = time.time()
  print(f"(t={end - start})")
