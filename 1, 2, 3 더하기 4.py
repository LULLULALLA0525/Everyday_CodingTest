import sys

input = lambda: sys.stdin.readline()

# 1로만 이루어진, 2로만 이루어진, 3으로만 이루어진, (1, 2)로만 이루어진, (2, 3)으로만 이루어진, (1, 3)으로만 이루어진, (1, 2, 3) 전부로 이루어진
ONLY1, ONLY2, ONLY3, ONLY12, ONLY23, ONLY13, ALL = list(range(7))

def solution(numbers):
  dp = [[0, 0, 0, 0, 0, 0, 0] for _ in range(max(numbers) + 1)]
  dp[1] = [1, 0, 0, 0, 0, 0, 0]   # 1
  dp[2] = [1, 1, 0, 0, 0, 0, 0]   # 1+1, 2
  dp[3] = [1, 0, 1, 1, 0, 0, 0]   # 1+1+1, 1+2, 3
  for i in range(4, max(numbers) + 1):
    PLUS1, PLUS2, PLUS3 = i - 1, i - 2, i - 3
    dp[i] = [
      dp[PLUS1][ONLY1],
      dp[PLUS2][ONLY2],
      dp[PLUS3][ONLY3],
      dp[PLUS1][ONLY2] + dp[PLUS1][ONLY12],
      dp[PLUS2][ONLY23] + dp[PLUS2][ONLY3],
      dp[PLUS1][ONLY3] + dp[PLUS1][ONLY13],
      dp[PLUS1][ONLY23] + dp[PLUS1][ALL]
    ]

  for number in numbers:
    print(sum(dp[number]))  

T = int(input())
NUMBERS = [int(input()) for _ in range(T)]
solution(NUMBERS)