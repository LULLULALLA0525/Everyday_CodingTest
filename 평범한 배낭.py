import sys

input = lambda: sys.stdin.readline()

WEIGHT, VALUE = 0, 1

def solution(n, k, items):
  dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
  items.insert(0, 0)

  for i in range(1, n + 1):
    for j in range(1, k + 1):
      if j < items[i][WEIGHT]:
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j] = max(dp[i - 1][j], items[i][VALUE] + dp[i - 1][j - items[i][WEIGHT]])

  return dp[n][k]
    
N, K = list(map(int, input().split()))
ITEMS = []
for _ in range(N):
  ITEMS.append(list(map(int, input().split())))
print(solution(N, K, ITEMS))