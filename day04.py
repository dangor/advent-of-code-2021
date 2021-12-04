def p1(input):
  file = open(input)
  (drawing, boards, index) = parse(file)
  file.close()

  (winning_board, draw) = play_bingo(drawing, boards, index)

  sum = 0
  for row in winning_board:
    for cell in row:
      if not cell['marked']:
        sum += cell['value']

  return sum * draw

def play_bingo(drawing, boards, index):
  for draw in drawing:
    for cell in index[draw]:
      cell['marked'] = True
      if is_winner(boards[cell['board']], cell):
        return (boards[cell['board']], draw)
  
  raise "no winner"

def is_winner(board, cell):
  if row_wins(board, cell['row']):
    return True
  if col_wins(board, cell['col']):
    return True
  return False

def row_wins(board, row):
  for i in range(len(board)):
    if not board[row][i]['marked']:
      return False
  return True

def col_wins(board, col):
  for i in range(len(board)):
    if not board[i][col]['marked']:
      return False
  return True

def parse(file):
  input = list(x.strip('\n') for x in file.readlines())
  drawing = list(map(int, input.pop(0).split(',')))
  boards = []
  index = {}

  while (len(input) > 0):
    line = input.pop(0)
    if line == "":
      continue

    board = []
    for i in range(5):
      row = []
      nums = line.split()
      for j in range(len(nums)):
        num = int(nums[j])
        cell = {
          'value': num,
          'board': len(boards),
          'row': i,
          'col': j,
          'marked': False
        }
        
        row.append(cell)
        
        if num not in index:
          index[num] = []
        index[num].append(cell)

      board.append(row)
      if len(input) > 0:
        line = input.pop(0)

    boards.append(board)

  return (drawing, boards, index)