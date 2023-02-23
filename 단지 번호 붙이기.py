import sys
from collections import deque
input = lambda: sys.stdin.readline()

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def solution(n, apt):
    num = [[0] * n for _ in range(n)]
    answer = []

    for row in range(n):
        for column in range(n):
            if apt[row][column] == 1 and num[row][column] == 0:
                answer.append(0)
                queue = deque()
                queue.append((row, column))
                while queue:
                    y, x = queue.popleft()
                    for dx, dy in d:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        elif apt[ny][nx] == 0:
                            continue
                        elif num[ny][nx] != 0:
                            continue
                        else:
                            queue.append((ny, nx))
                            num[ny][nx] = len(answer)
                            answer[-1] += 1

    answer = sorted(answer)
    print(len(answer))
    for i in answer:
        print(i)
    if len(answer) == 0:
        print(0)


N = int(input())
APT = []
for _ in range(N):
    APT.append(list(map(int, input().strip())))
solution(N, APT)