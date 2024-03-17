# def solution(n, tops):
#     dp = [[] for _ in range(n + 1)]
#     dp[0] = [2]
#     dp[1] = [1, 0, 2]
#     dp[2] = [1, 2, 2, 3]   # 모두 빈 것 + 1번 역삼각형이 채워지지 않은 + 2번 역삼각형이 채워지지 않은 + 둘 다 채워진
#     dp[3] = [1, 7, 4, 7, 4]
#     for i in range(2, n + 1):
#         dp[i] = [1]
#         for j in range(i):
#             dp[i].append((sum(dp[j]) - 1)*(sum(dp[i-j-1]) - 1))
#         dp[i].append(i + 1)

#     answer = sum(dp[n])
#     for i in range(len(tops)):
#         if tops[i] == 1:
#             answer += dp[n][i+1] + 1

#     return answer % 10007

# def solution(n, tops):
#     dp = [[] for _ in range(n + 1)]
#     dp[0] = [2]
#     dp[1] = [1, 0, 2]
#     # dp[2] = [1, 2, 2, 3]   # 모두 빈 것 + 1번 역삼각형이 채워지지 않은 + 2번 역삼각형이 채워지지 않은 + 둘 다 채워진
#     # dp[3] = [1, 7, 4, 7, 4]
#     for i in range(2, n + 1):
#         dp[i] = [1]
#         for j in range(i):
#             dp[i].append((sum(dp[j]) - 1)*(sum(dp[i-j-1]) - 1))
#         dp[i].append(i + 1)

#     answer = sum(dp[n])
#     for i in range(len(tops)):
#         if tops[i] == 1:
#             answer += dp[n][i+1] + 1

#     return answer % 10007

def solution(n, tops):

    dp = [[0, 0] for _ in range(n)]  # [오른쪽 구석을 사용하지 않은 경우의 수, 사용한 경우의 수]
    if tops[0] == 1:
        dp[0] = [3, 1]
    else:
        dp[0] = [2, 1]

    for i in range(1, n):
        if tops[i] == 1:
            dp[i] = [dp[i-1][0]*3 + dp[i-1][1]*2, dp[i-1][0] + dp[i-1][1]]
        else:
            dp[i] = [dp[i-1][0]*2 + dp[i-1][1], dp[i-1][0] + dp[i-1][1]]

    return sum(dp[n - 1]) % 10007

# 테스트 예시
print(solution(4, [1, 1, 0, 1]))  # 149
print(solution(2, [0, 1]))        # 11
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 7704