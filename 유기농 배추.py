import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

def solution(n, m, farm):
  bugs = 0

  for row in range(n):
    for column in range(m):
      if farm[row][column]:
        bugs += 1

        queue = deque()
        farm[row][column] = False
        queue.append((column, row))

        while(queue):
          x, y = queue.popleft()
          for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
              continue
            if farm[ny][nx]:
              farm[ny][nx] = False
              queue.append((nx, ny))

  return bugs

T = int(input())
ANSWERS = []
for _ in range(T):
  M, N, K = list(map(int, input().split()))
  FARM = [[False for _ in range(M)] for _ in range(N)]
  for _ in range(K):
    X, Y = list(map(int, input().split()))
    FARM[Y][X] = True
  ANSWERS.append(solution(N, M, FARM))
for ANSWER in ANSWERS:
  print(ANSWER)