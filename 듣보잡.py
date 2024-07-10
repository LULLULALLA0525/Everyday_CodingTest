import heapq
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

def solution(deutdo, bodo):
  DEUTDO_BODO = []
  for name in bodo:
    if DEUTDO[name]:
      heapq.heappush(DEUTDO_BODO, name)
  
  length = len(DEUTDO_BODO)
  print(length)
  for _ in range(length):
    print(heapq.heappop(DEUTDO_BODO))

N, M = list(map(int, input().split()))
DEUTDO = defaultdict(bool)
for _ in range(N):
  DEUTDO[input()] = True
BODO = []
for _ in range(M):
  BODO.append(input())
solution(DEUTDO, BODO)