import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def move(row, col, direction):
  rowMoves = [-1, 1, 0, 0]
  colMoves = [0, 0, -1, 1]
  return [row + rowMoves[direction], col + colMoves[direction]]

def solution(n, m, myMap):
  answer = [ [ -1 for _ in range(m) ] for _ in range(n) ]

  dest = [-1, -1]
  for row in range(n):
    for col in range(m):
      if myMap[row][col] == 2:
        dest = [row, col]
      elif myMap[row][col] == 0:
        answer[row][col] = 0

  queue = deque()
  queue.append(dest)
  answer[dest[0]][dest[1]] = 0
  while queue:
    row, col = queue.popleft()

    for direction in range(4):
      newRow, newCol = move(row, col, direction)

      if newRow < 0 or newCol < 0 or newRow >= n or newCol >= m:
        continue
      elif myMap[newRow][newCol] == 0:
        continue
      
      if answer[newRow][newCol] == -1 or answer[row][col] + 1 < answer[newRow][newCol]:
        answer[newRow][newCol] = answer[row][col] + 1
        queue.append([newRow, newCol])
  
  for row in answer:
    print(' '.join(list(map(str, row))))
  
N, M = list(map(int, input().split()))
MY_MAP = []
for _ in range(N):
  MY_MAP.append(list(map(int, input().split())))
solution(N, M, MY_MAP)