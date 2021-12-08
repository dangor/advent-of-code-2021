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
