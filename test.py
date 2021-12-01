def build_test(run_test):
  def test_case(input, expected):
    actual = run_test(input)
    assert actual == expected, f"Input: {input}\nActual: {actual}, Expected: {expected}"
  return test_case