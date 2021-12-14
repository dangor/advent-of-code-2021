def p1(input):
  file = open(input)
  (template, insertions) = parse(file)
  file.close()

  current = template

  for steps in range(10):
    new = ""
    for i in range(len(current) - 1):
      pair = current[i:i+2]
      new += pair[0] + insertions[pair]
    new += current[-1]
    current = new

  counts = {}

  for c in current:
    if c not in counts:
      counts[c] = 1
    else:
      counts[c] += 1

  return max(counts.values()) - min(counts.values())

def parse(file):
  lines = list(x.strip('\n') for x in file.readlines())

  template = lines.pop(0)
  lines.pop(0)

  insertions = {}

  for line in lines:
    parts = line.split(' -> ')
    insertions[parts[0]] = parts[1]

  return (template, insertions)