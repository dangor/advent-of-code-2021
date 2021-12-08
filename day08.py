def p1(input):
  file = open(input)
  outputs = list(x.strip('\n').split(' | ')[1] for x in file.readlines())
  file.close()

  sum = 0

  for output in outputs:
    pieces = output.split(' ')
    for piece in pieces:
      segments = len(piece)
      if segments == 2 or segments == 3 or segments == 4 or segments == 7:
        sum += 1
  
  return sum

def p2(input):
  file = open(input)
  lines = list(x.strip('\n').split(' | ') for x in file.readlines())
  file.close()

  sum = 0

  for line in lines:
    inputs = line[0].split(' ')
    outputs = line[1].split(' ')
    both = inputs + outputs

    one = set(find_part(both, 2))
    four = set(find_part(both, 4))

    output_digits = ""

    for output in outputs:
      segments = len(output)
      if segments == 2:
        output_digits += "1"
      elif segments == 3:
        output_digits += "7"
      elif segments == 4:
        output_digits += "4"
      elif segments == 7:
        output_digits += "8"
      else:
        output_set = set(output)
        if segments == 5: # 2, 3, 5
          if len(output_set.intersection(one)) == 2:
            output_digits += "3"
          elif len(output_set.intersection(four)) == 3:
            output_digits += "5"
          else:
            output_digits += "2"
        elif segments == 6: # 0, 6, 9
          if len(output_set.intersection(one)) == 1:
            output_digits += "6"
          elif len(output_set.intersection(four)) == 4:
            output_digits += "9"
          else:
            output_digits += "0"

    sum += int(output_digits)

  return sum

def find_part(parts, segments):
  for x in parts:
    if len(x) == segments:
      return x
  raise f"couldn't find {segments} segments"