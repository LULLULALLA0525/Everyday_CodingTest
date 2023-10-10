import sys
from itertools import combinations

input = lambda: sys.stdin.readline()

def solution(cows, m):
  cases = combinations(cows, m)
  weights = list(set([sum(case) for case in cases]))

  result = list(filter(
    lambda x: isPrime(x),
    weights
  ))

  if len(result) == 0:
    return "-1"
  else:
    return " ".join(map(str, sorted(result)))

def isPrime(num):
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

N, M = list(map(int, input().split()))
COWS = list(map(int, input().split()))
print(solution(COWS, M))