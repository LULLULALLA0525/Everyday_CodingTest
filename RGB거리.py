import sys

input = lambda: sys.stdin.readline()

INDEX, VALUE = 0, 1
MIN, MED, MAX = 0, 1, 2

def solution(n, cost):
  cost = sorted(cost, key=lambda x:x[VALUE])
  dp = [0] * n
  log = [0] * n

  dp[0] = cost[0][MIN][VALUE]
  log[0] = cost[0][MIN][INDEX]

  
  return n

N = int(input())
COST = []
for _ in range(N):
  TEMP = list(map(int, input().split()))
  COST.append([(i, TEMP[i]) for i in range(3)])
print(solution(N, COST))