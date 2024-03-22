import sys

input = lambda: sys.stdin.readline()

CHOICE, VALUE = 0, 1

def solution(n, stickers):
  dp = [[0 for _ in range(n)] for _ in range(2)]

  for i in range(n):
    for p in range(2):
      compare = [0]
      if i >= 1:
        compare.append(dp[p ^ 1][i - 1])
      if i >= 2:
        compare.append(dp[p][i - 2])
        compare.append(dp[p ^ 1][i - 2])
      dp[p][i] = max(compare) + stickers[p][i]

  return max(dp[0][n - 1], dp[1][n - 1])

T = int(input())
results = []
for _ in range(T):
  N = int(input())
  STICKERS = []
  for _ in range(2):
    STICKERS.append(list(map(int, input().split())))
  results.append(solution(N, STICKERS))

for result in results:
  print(result)