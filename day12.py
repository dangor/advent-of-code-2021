from copy import copy

def p1(input):
  file = open(input)
  lines = list(x.strip('\n') for x in file.readlines())
  file.close()

  nodes = {}

  def add_node(node, neighbor):
    if node not in nodes:
      nodes[node] = [neighbor]
    else:
      nodes[node].append(neighbor)

  for line in lines:
    parts = line.split('-')
    add_node(parts[0], parts[1])
    add_node(parts[1], parts[0])

  count = count_paths(nodes)

  return count

def count_paths(nodes, node = 'start', visited = []):
  if node.islower():
    visited.append(node)
  if node == 'end':
    return 1
  total = 0
  for neighbor in nodes[node]:
    if neighbor not in visited:
      total += count_paths(nodes, neighbor, copy(visited))
  return total