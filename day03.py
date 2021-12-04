def p1(input):
  file = open(input)
  strings = list(x.strip('\n') for x in file.readlines())
  file.close()

  return power_consumption(strings)

# O(n), string manipulation
def power_consumption(strings):
  acc = []

  def process_string(string):
    for i in range(len(string)):
      if len(acc) <= i:
        acc.append([0,0])
      bit = int(string[i])
      acc[i][bit] += 1
  
  for string in strings:
    process_string(string)

  gamma = ""
  epsilon = ""

  for pos in acc:
    if pos[0] > pos[1]:
      gamma += "0"
      epsilon += "1"
    elif pos[1] > pos[0]:
      gamma += "1"
      epsilon += "0"
    else:
      raise "counts are equal"

  return int(gamma, 2) * int(epsilon, 2)