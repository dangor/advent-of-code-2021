openers = "([{<"
closers = ")]}>"
points = [3, 57, 1197, 25137]

def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  sum = 0

  for line in lines:
    stack = []
    for c in line:
      if c in openers:
        stack.append(c)
      else:
        opener = stack.pop()
        i = closers.find(c)
        if opener != openers[i]:
          # corrupt
          sum += points[i]
  
  return sum

def p2(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  scores = []

  for line in lines:
    stack = []
    corrupt = False

    for c in line:
      if c in openers:
        stack.append(c)
      else:
        opener = stack.pop()
        i = closers.find(c)
        if opener != openers[i]:
          # corrupt
          corrupt = True
          break
    
    if corrupt:
      continue

    score = 0

    stack.reverse()
    for o in stack:
      score *= 5
      score += openers.find(o) + 1

    scores.append(score)

  scores.sort()

  return scores[len(scores)//2]
