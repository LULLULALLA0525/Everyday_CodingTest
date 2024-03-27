import sys

input = sys.stdin.readline

DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

RED, BLUE = 0, 1
ROW, COLUMN = 0, 1

def move_ball(board, position, direction):
  if direction == "UP":
    for r in range(position[ROW] - 1, -1, -1):
      if board[r][position[COLUMN]] == "O":
        return (-1, -1)
      elif board[r][position[COLUMN]] != ".":
        return (r + 1, position[COLUMN])
  elif direction == "DOWN":
    for r in range(position[ROW] + 1, len(board)):
      if board[r][position[COLUMN]] == "O":
        return (-1, -1)
      elif board[r][position[COLUMN]] != ".":
        return (r - 1, position[COLUMN])
  elif direction == "LEFT":
    for c in range(position[COLUMN] - 1, -1, -1):
      if board[position[ROW]][c] == "O":
        return (-1, -1)
      elif board[position[ROW]][c] != ".":
        return (position[ROW], c + 1)
  elif direction == "RIGHT":
    for c in range(position[COLUMN] + 1, len(board[0])):
      if board[position[ROW]][c] == "O":
        return (-1, -1)
      elif board[position[ROW]][c] != ".":
        return (position[ROW], c - 1)

def move(board, position, direction, step):
  if step > 10:
    return 11
  
  new_position = [(0, 0), (0, 0)]
  new_board = [copy[:] for copy in board]

  if (direction == "UP" and position[RED][ROW] <= position[BLUE][ROW]) or (direction == "DOWN" and position[RED][ROW] >= position[BLUE][ROW]) or (direction == "LEFT" and position[RED][COLUMN] <= position[BLUE][COLUMN]) or (direction == "RIGHT" and position[RED][COLUMN] >= position[BLUE][COLUMN]):
    new_position[RED] = move_ball(new_board, position[RED], direction)
    new_board[position[RED][ROW]][position[RED][COLUMN]] = "."
    if new_position[RED] != (-1, -1):
      new_board[new_position[RED][ROW]][new_position[RED][COLUMN]] = "R"

    new_position[BLUE] = move_ball(new_board, position[BLUE], direction)
    new_board[position[BLUE][ROW]][position[BLUE][COLUMN]] = "."
    if new_position[BLUE] != (-1, -1):
      new_board[new_position[BLUE][ROW]][new_position[BLUE][COLUMN]] = "B"
  else:
    new_position[BLUE] = move_ball(new_board, position[BLUE], direction)
    new_board[position[BLUE][ROW]][position[BLUE][COLUMN]] = "."
    if new_position[BLUE] != (-1, -1):
      new_board[new_position[BLUE][ROW]][new_position[BLUE][COLUMN]] = "B"

    new_position[RED] = move_ball(new_board, position[RED], direction)
    new_board[position[RED][ROW]][position[RED][COLUMN]] = "."
    if new_position[RED] != (-1, -1):
      new_board[new_position[RED][ROW]][new_position[RED][COLUMN]] = "R"

  if new_position[BLUE] == (-1, -1):
    return 11
  elif new_position[RED] == (-1, -1):
    return step
  else:
    min_value = 11
    for d in DIRECTIONS:
      if d != direction:
        min_value = min(min_value, move(new_board, new_position, d, step + 1))
    return min_value

def solution(n, m, board):
  position = [(0, 0), (0, 0)]

  for row in range(n):
    for col in range(m):
      if board[row][col] == "R":
        position[RED] = (row, col)
      elif board[row][col] == "B":
        position[BLUE] = (row, col)

  answer = 11
  for direction in DIRECTIONS:
    answer = min(answer, move(board, position, direction, 1))

  if answer == 11:
    return -1
  else:
    return answer

N, M = list(map(int, input().split()))
BOARD = []
for _ in range(N):
  BOARD.append(list(input().rstrip()))
print(solution(N, M, BOARD))