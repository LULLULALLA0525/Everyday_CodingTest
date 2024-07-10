import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, stairs):
  dp = [(0, 0) for _ in range(n)]   #(직전 칸에서 올라온 경우, 두 칸 아래서 올라온 경우)
  dp[0] = (stairs[0], stairs[0])
  if n > 1:
    dp[1] = (stairs[0] + stairs[1], stairs[1])

  for i in range(2, n):
    dp[i] = (dp[i - 1][1] + stairs[i], max(dp[i - 2]) + stairs[i])
  
  return max(dp[n - 1])

N = int(input())
STAIRS = []
for _ in range(N):
  STAIRS.append(int(input()))
print(solution(N, STAIRS))