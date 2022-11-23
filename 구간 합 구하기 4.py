import sys

input = lambda: sys.stdin.readline()


N, M = list(map(int, input().split()))
NUMS = list(map(int, input().split()))
SUMS = [0]
for i in range(1, N + 1):
    SUMS.append(SUMS[i - 1] + NUMS[i - 1])
for _ in range(M):
    I, J = list(map(int, input().split()))
    print(SUMS[J] - SUMS[I - 1])
