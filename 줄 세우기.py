import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline()

def solution(n, m, compares):
  graph = defaultdict(list)
  degree = [0 for _ in range(n + 1)]

  for compare in compares:
    big, small = compare
    graph[big].append(small)
    degree[small] += 1

  queue = deque()
  for i in range(1, n + 1):
    if degree[i] == 0:
      queue.append(i)

  answer = []
  while queue:
    index = queue.popleft()

    if degree[index] != 0:
      continue

    answer.append(str(index))

    degree[index] = -1
    for node in graph[index]:
      if degree[node] > 0:
        degree[node] -= 1
        if degree[node] == 0:
          queue.append(node)

  print(" ".join(answer))

N, M = list(map(int, input().split()))
COMPARES = []
for _ in range(M):
  COMPARES.append(list(map(int, input().split())))
solution(N, M, COMPARES)