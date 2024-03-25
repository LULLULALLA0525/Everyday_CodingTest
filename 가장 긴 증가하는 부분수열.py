import sys

input = lambda: sys.stdin.readline()

def solution(n, array):
  dp = [0 for _ in range(n)]

  dp[0] = 1
  for i in range(1, n):
    max_value = 0
    for j in range(i):
      if array[j] < array[i]:
        max_value = max(max_value, dp[j])
    dp[i] = max_value + 1

  return max(dp)

N = int(input())
ARRAY = list(map(int, input().split()))
print(solution(N, ARRAY))