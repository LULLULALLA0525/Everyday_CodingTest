import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline()

def solution(n, array):
  dp = []

  for num in array:
    if len(dp) == 0:
      dp.append(num)
    else:
      if num > dp[-1]:
        dp.append(num)
      else:
        index = bisect_left(dp, num)
        dp[index] = num

  return len(dp)

N = int(input())
ARRAY = list(map(int, input().split()))
print(solution(N, ARRAY))