import sys
from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline()

def solution(n, m, numbers):
  numbers = sorted(numbers)
  results = combinations_with_replacement(numbers, m)
  for result in results:
    print(*result)

N, M = list(map(int, input().split()))
NUMBERS = list(map(int, input().split()))
solution(N, M, NUMBERS)