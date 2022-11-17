import sys

input = lambda: sys.stdin.readline()


def solution(n):
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
    for i in range(12, n + 1):
        p.append(p[i - 1] + p[i - 5])
    return p[n]


T = int(input())
for _ in range(T):
    N = int(input())
    print(solution(N))
