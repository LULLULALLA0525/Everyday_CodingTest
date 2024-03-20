import sys
import heapq

input = lambda: sys.stdin.readline()
print = lambda x: sys.stdout.write(x + "\n")

START, END, WEIGHT = 0, 1, 2
INF = 11

def solution(v, k, edges):
  edges_by_nodes = [[] for _ in range(v + 1)]
  for edge in edges:
    edges_by_nodes[edge[START]].append((edge[START], edge[END], edge[WEIGHT]))

  costs = [v * INF for _ in range(v + 1)]
  visited = [False for _ in range(v + 1)]
  costs[k] = 0

  queue = []
  heapq.heappush(queue, (0, k))

  while queue:
    weight, current = heapq.heappop(queue)

    if visited[current]:
      continue
    visited[current] = True

    for edge in edges_by_nodes[current]:
      if weight + edge[WEIGHT] < costs[edge[END]]:
        costs[edge[END]] = weight + edge[WEIGHT]
        heapq.heappush(queue, (costs[edge[END]], edge[END]))

  for i in range(1, v + 1):
    if costs[i] == v * INF:
      print("INF")
    else:
      print(str(costs[i]))

V, E = list(map(int, input().split()))
K = int(input())
EDGES = []
for _ in range(E):
  EDGES.append(list(map(int, input().split())))
solution(V, K, EDGES)