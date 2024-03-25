import heapq
import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline()

def solution(v, e, graph):
  answer = 0

  connected = [False for _ in range(v + 1)]
  connected[0] = True

  queue = []
  connected[1] = True
  while graph[1]:
    edge = heapq.heappop(graph[1])
    heapq.heappush(queue, edge)

  while not all(connected):
    weight, node = heapq.heappop(queue)

    if connected[node]:
      continue
    
    answer += weight
    connected[node] = True

    while graph[node]:
      edge = heapq.heappop(graph[node])
      heapq.heappush(queue, edge)

  return answer

V, E = list(map(int, input().split()))
GRAPH = defaultdict(list)
for _ in range(E):
  A, B, W = list(map(int, input().split()))
  heapq.heappush(GRAPH[A], (W, B))
  heapq.heappush(GRAPH[B], (W, A))

print(solution(V, E, GRAPH))