import sys

input = lambda: sys.stdin.readline()


def solution(n, stairs):
    dp = [[0, 0], [0, stairs[1]], [1, stairs[1] + stairs[2]]]
    for i in range(3, n + 1):
        dp.append([0, 0])
        if dp[i - 1][0] == 1:
            dp[i][0] = 0
            dp[i][1] = dp[i - 2][1] + stairs[i]
        else:
            if dp[i - 1][1] > dp[i - 2][1]:
                dp[i][0] = 1
                dp[i][1] = dp[i - 1][1] + stairs[i]
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i - 2][1] + stairs[i]
    return dp[n][1]


N = int(input())
STAIRS = [0]
for _ in range(N):
    STAIRS.append(int(input()))
print(solution(N, STAIRS))
