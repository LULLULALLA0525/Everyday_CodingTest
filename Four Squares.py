import sys

input = lambda: sys.stdin.readline()


def solution(n):
    if dp[n] <= 4:
        return dp[n]

    square = int(n ** (1 / 2))
    for j in range(square, 0, -1):
        dp[n] = min(dp[n], solution(n - j**2) + 1)
        if dp[n] <= 2:
            break

    return dp[n]


N = int(input())
dp = [5] * (N + 1)
dp[0] = 0
print(solution(N))
