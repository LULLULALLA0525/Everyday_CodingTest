import sys

input = lambda: sys.stdin.readline().rstrip()

ROW, COL = 0, 1

def find_heart(board):
  for row in range(len(board)):
    for col in range(len(board)):
      if board[row][col] == '*':
        return [row + 1, col]

def solution(board):
  heart = find_heart(board)

  left_arm = 0
  right_arm = 0
  for col in range(len(board)):
    if board[heart[ROW]][col] == '*':
      if col < heart[COL]:
        left_arm += 1
      elif col > heart[COL]:
        right_arm += 1

  body = 0
  for row in range(heart[ROW] + 1, len(board)):
    if board[row][heart[COL]] != '*':
      break
    body += 1

  left_leg = 0
  for row in range(heart[ROW] + body + 1, len(board)):
    if board[row][heart[COL] - 1] != '*':
      break
    left_leg += 1

  right_leg = 0
  for row in range(heart[ROW] + body + 1, len(board)):
    if board[row][heart[COL] + 1] != '*':
      break
    right_leg += 1

  print(' '.join(map(str, [heart[ROW] + 1, heart[COL] + 1])))
  print(' '.join(map(str, [left_arm, right_arm, body, left_leg, right_leg])))

N = int(input())
BOARD = []
for _ in range(N):
  BOARD.append(list(input()))
solution(BOARD)