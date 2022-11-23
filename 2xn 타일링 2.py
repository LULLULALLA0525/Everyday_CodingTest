import sys

input = lambda: sys.stdin.readline()


def solution(n):
    dp = [0, 1, 3]
    for i in range(3, n + 2):
        dp.append(dp[i - 1] + 2 * dp[i - 2])
    return dp[n] % 10007


N = int(input())
print(solution(N))
