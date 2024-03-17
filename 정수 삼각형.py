import sys

input = lambda: sys.stdin.readline()

def solution(n, triangle):
  dp = [triangle[0]]

  for i in range(1, n):
    floor = []
    for j in range(i + 1):
      if j == 0:
        floor.append(triangle[i][j] + dp[i - 1][0])
      elif j == i:
        floor.append(triangle[i][j] + dp[i - 1][-1])
      else:
        floor.append(triangle[i][j] + max(dp[i - 1][j - 1: j + 1]))
    dp.append(floor)

  return max(dp[n - 1])

N = int(input())
TRIANGLE = []
for _ in range(N):
  TRIANGLE.append(list(map(int, input().split())))
print(solution(N, TRIANGLE))