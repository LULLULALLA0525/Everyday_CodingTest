def solution(n, tops):
    dp = [[] for _ in range(n + 1)]
    dp[0] = [2]
    dp[1] = [1, 0, 2]
    dp[2] = [1, 2, 2, 3]   # 모두 빈 것 + 1번 역삼각형이 채워지지 않은 + 2번 역삼각형이 채워지지 않은 + 둘 다 채워진
    dp[3] = [1, 7, 4, 7, 4]
    for i in range(2, n + 1):
        dp[i] = [1]
        for j in range(i):
            dp[i].append((sum(dp[j]) - 1)*(sum(dp[i-j-1]) - 1))
        dp[i].append(i + 1)

    answer = sum(dp[n])
    for i in range(len(tops)):
        if tops[i] == 1:
            answer += dp[n][i+1] + 1

    return answer % 10007

def solution(n, tops):
    dp = [[] for _ in range(n + 1)]
    dp[0] = [2]
    dp[1] = [1, 0, 2]
    # dp[2] = [1, 2, 2, 3]   # 모두 빈 것 + 1번 역삼각형이 채워지지 않은 + 2번 역삼각형이 채워지지 않은 + 둘 다 채워진
    # dp[3] = [1, 7, 4, 7, 4]
    for i in range(2, n + 1):
        dp[i] = [1]
        for j in range(i):
            dp[i].append((sum(dp[j]) - 1)*(sum(dp[i-j-1]) - 1))
        dp[i].append(i + 1)

    answer = sum(dp[n])
    for i in range(len(tops)):
        if tops[i] == 1:
            answer += dp[n][i+1] + 1

    return answer % 10007