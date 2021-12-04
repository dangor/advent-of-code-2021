def p1(input):
  file = open(input)
  strings = list(x.strip('\n') for x in file.readlines())
  file.close()

  return power_consumption(strings)

def p2(input):
  file = open(input)
  strings = list(x.strip('\n') for x in file.readlines())
  file.close()

  return life_support(strings)

# O(n), string manipulation
def power_consumption(strings):
  acc = process_strings(strings)

  gamma = ""
  epsilon = ""

  for pos in acc:
    if len(pos[0]) > len(pos[1]):
      gamma += "0"
      epsilon += "1"
    elif len(pos[1]) > len(pos[0]):
      gamma += "1"
      epsilon += "0"
    else:
      raise "counts are equal"

  return int(gamma, 2) * int(epsilon, 2)

def life_support(strings):
  o2_strings = co2_strings = strings
  o2_index = co2_index = 0

  while(len(o2_strings) > 1):
    acc = process_strings(o2_strings)

    pos = acc[o2_index]
    if len(pos[0]) > len(pos[1]):
      o2_strings = pos[0]
    else:
      o2_strings = pos[1]
    o2_index += 1

  while(len(co2_strings) > 1):
    acc = process_strings(co2_strings)

    pos = acc[co2_index]
    if len(pos[0]) > len(pos[1]):
      co2_strings = pos[1]
    else:
      co2_strings = pos[0]
    co2_index += 1

  return int(o2_strings[0], 2) * int(co2_strings[0], 2)

def process_strings(strings):
  acc = []

  for string in strings:
    for i in range(len(string)):
      if len(acc) <= i:
        acc.append([[],[]])
      bit = int(string[i])
      acc[i][bit].append(string)
  
  return acc