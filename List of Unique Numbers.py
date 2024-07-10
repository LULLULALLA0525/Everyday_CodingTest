import sys
from collections import defaultdict

input = lambda: sys.stdin.readline()

def solution(n, numbers):
  reachableToLeft = []
  lastAppeared = defaultdict(lambda: -1)
  for i in range(n):
    if i == 0:
      reachableToLeft.append(1)
    else:
      mine = i - lastAppeared[numbers[i]]
      reachableToLeft.append(min(mine, reachableToLeft[i - 1] + 1))
    lastAppeared[numbers[i]] = i

  return sum(reachableToLeft)

N = int(input())
NUMBERS = list(map(int, input().split()))
print(solution(N, NUMBERS))