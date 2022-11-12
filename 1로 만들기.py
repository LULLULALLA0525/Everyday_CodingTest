INF = 10000000


N = int(input())
dp = [0] * (N + 1)
for i in range(2, N + 1):
    candidate = [INF] * 3
    if i % 3 == 0:
        candidate[0] = dp[i // 3] + 1
    if i % 2 == 0:
        candidate[1] = dp[i // 2] + 1
    candidate[2] = dp[i - 1] + 1
    dp[i] = min(candidate)
print(dp[N])
