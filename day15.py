from heapq import heappush, heappop

def p1(input):
  file = open(input)
  board = list(list(map(int, list(x.strip('\n')))) for x in file.readlines())
  file.close()

  current = (0, 0)
  goal = (len(board) - 1, len(board[0]) - 1)
  visited = set([current])
  h = []
  heappush(h, (0, current))

  while len(h) > 0:
    (risk, lowest) = heappop(h)
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for offset in offsets:
      x = offset[0] + lowest[0]
      y = offset[1] + lowest[1]
      if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0:
        continue

      new_risk = risk + board[x][y]
      if (x, y) == goal:
        return new_risk
      if (x, y) in visited:
        continue
      visited.add((x, y))
      heappush(h, (new_risk, (x, y)))
