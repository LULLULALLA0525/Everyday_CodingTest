import sys

input = lambda: sys.stdin.readline()


def solution(a, b):
    result = 1
    for _ in range(b):
        result *= a
        result %= 10
    return result


T = int(input())
for i in range(T):
    A, B = list(map(int, input().split()))
    print(solution(A, B))
