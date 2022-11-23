import sys
from collections import deque

input = lambda: sys.stdin.readline()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


T = int(input())
for _ in range(T):
    M, N, K = list(map(int, input().split()))
    FARM = [[0] * M for _ in range(N)]
    VISITED = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = list(map(int, input().split()))
        FARM[Y][X] = 1
    answer = 0
    queue = deque()
    for y in range(N):
        for x in range(M):
            if FARM[y][x] == 1 and not VISITED[y][x]:
                answer += 1
                queue.append((x, y))
                while queue:
                    xx, yy = queue.popleft()
                    VISITED[yy][xx] = True
                    for i in range(4):
                        nx = xx + dx[i]
                        ny = yy + dy[i]
                        if nx < 0 or nx >= M or ny < 0 or ny >= N:
                            continue
                        if FARM[ny][nx] == 1 and not VISITED[ny][nx]:
                            queue.append((nx, ny))
    print(answer)
