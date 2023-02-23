import sys
from collections import deque
input = lambda: sys.stdin.readline()

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solution(n, m, maze):
    cost = [[0] * m for _ in range(n)]
    cost[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            elif maze[ny][nx] == 0:
                continue
            elif cost[ny][nx] == 0:
                cost[ny][nx] = cost[y][x] + 1
                queue.append((nx, ny))

    return cost[n - 1][m - 1]


N, M = list(map(int, input().split()))
MAZE = []
for _ in range(N):
    MAZE.append(list(map(int, input().strip())))
print(solution(N, M, MAZE))