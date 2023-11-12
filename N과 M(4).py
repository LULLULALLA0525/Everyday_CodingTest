import sys
from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline()

def solution(n, m):
  results = combinations_with_replacement(range(1, n+1), m)
  for result in results:
    print(*result)

N, M = list(map(int, input().split()))
solution(N, M)