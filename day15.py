from heapq import heappush, heappop

def p1(input):
  file = open(input)
  board = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  return traverse(board)

def p2(input):
  file = open(input)
  board = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  for tile in range(4):
    for i in range(len(board)):
      for j in range(len(board)):
        board[i].append(board[i][j + tile * len(board)] + 1)

  height = len(board)
  for tile in range(4):
    for i in range(height):
      row = []
      for j in range(len(board[0])):
        row.append(board[i + tile * height][j] + 1)
      board.append(row)
  
  return traverse(board)

def traverse(board):
  current = (0, 0)
  goal = (len(board) - 1, len(board[0]) - 1)
  visited = set([current])
  h = []
  heappush(h, (0, current))

  while len(h) > 0:
    (risk, lowest) = heappop(h)
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)] # another subreddit clue: the trick is to go all 4 directions, not just down or right.
    for offset in offsets:
      x = offset[0] + lowest[0]
      y = offset[1] + lowest[1]
      if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0:
        continue

      new_risk = risk + ((board[x][y] - 1) % 9) + 1
      if (x, y) == goal:
        return new_risk
      if (x, y) in visited:
        continue
      visited.add((x, y))
      heappush(h, (new_risk, (x, y)))

