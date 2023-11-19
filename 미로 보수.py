import sys
from collections import deque

input = lambda: sys.stdin.readline()

directions = ["U", "L", "D", "R"]
dr = {"U": -1, "D": 1, "L": 0, "R": 0}
dc = {"U": 0, "D": 0, "L": -1, "R": 1}

def dfs(maze, visited, row, column, path):
  nr, nc = row + dr[maze[row][column]], column + dc[maze[row][column]]
  if visited[nr][nc]:
    return []
  elif [nr, nc] not in path:
    return dfs(maze, visited, nr, nc, path + [[nr, nc]])
  else:
    return path + [[nr, nc]]


def solution(maze, cost):
  escape = [ [False for _ in range(len(row))] for row in maze ]
  for row in range(len(maze)):
    for column in range(len(maze[row])):
      if not escape[row][column]:
        nr, nc = row + dr[maze[row][column]], column + dc[maze[row][column]]
        if nr < 0 or nr >= len(maze) or nc < 0 or nc >= len(maze[row]):
          # 탈출할 수 있는 통로!
          # 주변에서 이어지는 경로 확인
          queue = deque()
          queue.append([row, column])
          while queue:
            r, c = queue.popleft()
            escape[r][c] = True
            for i in range(4):
              direction = directions[i]
              br, bc = r + dr[direction], c + dc[direction]
              if br < 0 or br >= len(maze) or bc < 0 or bc >= len(maze[row]):
                continue
              opposite = directions[(i+2) % 4]
              if maze[br][bc] == opposite:
                queue.append([br, bc])

  visited = [ [False for _ in range(len(row))] for row in maze ]
  loop_num = [ [0 for _ in range(len(row))] for row in maze ]
  current_num = 0
  for row in range(len(maze)):
    for column in range(len(maze[row])):
      if not escape[row][column] and not visited[row][column]:
        path = dfs(maze, visited, row, column, [[row, column]])
        if path:
          loop_started = False
          for room in path:
            visited[room[0]][room[1]] = True
            if not loop_started and room == path[-1]:
              current_num += 1
              loop_started = True
            if loop_started:
              loop_num[room[0]][room[1]] = current_num
            
  result = 0
  for num in range(1, current_num + 1):
    min_cost = 501
    for row in range(len(maze)):
      for column in range(len(maze[row])):
        if loop_num[row][column] == num:
          min_cost = min(min_cost, cost[row][column])
    result += min_cost

  return result

N, M = list(map(int, input().split()))
MAZE = [list(input().strip()) for _ in range(N)]
COST = [list(map(int, input().split())) for _ in range(N)]
print(solution(MAZE, COST))