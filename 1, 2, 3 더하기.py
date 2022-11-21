import sys

input = lambda: sys.stdin.readline()


def solution(n):
    if n <= 3:
        dp = [0, 1, 2, 4]
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2   # 1+1       2
        dp[3] = 4   # 1+1+1     1+2     2+1     3
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


N = int(input())
for _ in range(N):
    print(solution(int(input())))
