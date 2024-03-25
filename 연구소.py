import sys
from collections import deque
from itertools import combinations

input = lambda: sys.stdin.readline()

EMPTY, WALL, VIRUS = 0, 1, 2

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(n, m, lab):
  answer = 0

  empty_spaces = []
  viruses = []
  for row in range(n):
    for col in range(m):
      if lab[row][col] == EMPTY:
        empty_spaces.append((row, col))
      elif lab[row][col] == VIRUS:
        viruses.append((row, col))

  wall_cases = combinations(empty_spaces, 3)

  for walls in wall_cases:
    simulate_lab = [copy[:] for copy in lab]
    remain_spaces = len(empty_spaces)

    # 벽 설치
    for wall in walls:
      row, col = wall
      simulate_lab[row][col] = WALL
      remain_spaces -= 1

    # 바이러스 전염
    queue = deque()
    for virus in viruses:
      queue.append(virus)

    while queue:
      y, x = queue.popleft()

      if simulate_lab[y][x] == EMPTY:
        simulate_lab[y][x] = VIRUS
        remain_spaces -= 1

      if remain_spaces <= answer:
        break
      
      for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
          continue
        if simulate_lab[ny][nx] == EMPTY:
          queue.append((ny, nx))
    
    answer = max(answer, remain_spaces)
    
  return answer

N, M = list(map(int, input().split()))
LAB = []
for _ in range(N):
  LAB.append(list(map(int, input().split())))
print(solution(N, M, LAB))