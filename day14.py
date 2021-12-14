from copy import copy

# brute force
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

# i gave up and looked up a clue on the subreddit which was (spoiler) to keep a separate map of pairs.
def p2(input):
  file = open(input)
  (template, insertions) = parse(file)
  file.close()

  # init
  init = {}
  counts = {}
  for pair in insertions.keys():
    init[pair] = 0
    if insertions[pair] not in counts:
      counts[insertions[pair]] = 0

  current = copy(init)

  # seed
  for i in range(len(template) - 1):
    counts[template[i]] += 1
    pair = template[i:i+2]
    current[pair] += 1
  counts[template[-1]] += 1

  # step through
  for step in range(40):
    new = copy(init)
    for pair in current.keys():
      count = current[pair]
      insertion = insertions[pair]
      counts[insertion] += count
      p1 = pair[0] + insertion
      p2 = insertion + pair[1]
      new[p1] += count
      new[p2] += count
    current = new

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