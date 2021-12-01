from test import build_test

def p1(input):
  output = num_valid(input)
  print(output)

def p2(input):
  output = num_valid(input, doubles_only = True)
  print(output)

def num_valid(input, doubles_only = False):
  lower, upper = input[0], input[1]
  count = 0
  for i in range(lower, upper + 1):
    if is_valid(i, doubles_only):
      count += 1
  return count

def is_valid(num, doubles_only = False):
  has_double = False
  has_at_least_double = False
  double_count = 1
  previous_digit = None
  digit_mask = 100000
  remaining = num
  while digit_mask > 0:
    digit = remaining // digit_mask

    if previous_digit != None and previous_digit == digit:
      has_at_least_double = True
      double_count += 1
    else:
      if double_count == 2:
        has_double = True
      double_count = 1

    if previous_digit != None and previous_digit > digit:
      return False # decreasing
    
    previous_digit = digit

    remaining %= digit_mask
    digit_mask //= 10

  if double_count == 2:
    has_double = True

  if doubles_only:
    return has_double
  else:
    return has_at_least_double

def test():
  test_case = build_test(is_valid)
  test_case(122345, True)
  test_case(111111, True)
  test_case(223450, False)
  test_case(123789, False)

  def is_valid_p2(num):
    return is_valid(num, doubles_only = True)
  
  test_case = build_test(is_valid_p2)
  test_case(122345, True)
  test_case(111111, False)
  test_case(223450, False)
  test_case(123789, False)
  test_case(112233, True)
  test_case(123444, False)
  test_case(111122, True)
