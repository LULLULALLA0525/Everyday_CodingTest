import sys
from itertools import permutations

input = lambda: sys.stdin.readline()

def solution(n, m, numbers):
  numbers = sorted(numbers)
  results = permutations(numbers, m)
  for result in sorted(list(set(results))):
    print(*result)

N, M = list(map(int, input().split()))
NUMBERS = list(map(int, input().split()))
solution(N, M, NUMBERS)