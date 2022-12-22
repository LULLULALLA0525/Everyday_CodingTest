import sys

input = lambda: sys.stdin.readline()


def solution(n):
    if n[0] == n[1] and n[1] == n[2]:
        return 10000+(1000*n[0])
    elif n[0] == n[1] or n[0] == n[2]:
        return 1000+(100*n[0])
    elif n[1] == n[2]:
        return 1000+(100*n[1])
    else:
        return max(n)*100


N = list(map(int, input().split()))
print(solution(N))
