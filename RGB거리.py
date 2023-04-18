import sys

input = lambda: sys.stdin.readline()

def solution(n, cost):
  dp = [[0, 0, 0] for _ in range(n)]
  dp[0] = cost[0]

  for i in range(1, n):
    for j in range(3):
      dp[i][j] = cost[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

  return min(dp[n - 1])

N = int(input())
COST = []
for _ in range(N):
  COST.append(list(map(int, input().split())))
print(solution(N, COST))