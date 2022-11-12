N = int(input())
DP = [[1, 0, 0], [0, 1, 1]]
for i in range(2, 41):
    DP.append([DP[i - 1][j] + DP[i - 2][j] for j in range(3)])
for _ in range(N):
    Q = int(input())
    print(DP[Q][0], DP[Q][1])
