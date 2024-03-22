import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline()

def solution(n, tree):
  parent = [0 for _ in range(n + 1)]

  queue = deque()
  queue.append(1)
  while queue:
    node = queue.popleft()
    for nest in tree[node]:
      if nest != parent[node]:
        parent[nest] = node
        queue.append(nest)
  
  for i in range(2, n + 1):
    print(parent[i])

N = int(input())
TREE = defaultdict(lambda: [])
for _ in range(N - 1):
  FIRST, SECOND = list(map(int, input().split()))
  TREE[FIRST].append(SECOND)
  TREE[SECOND].append(FIRST)
solution(N, TREE)