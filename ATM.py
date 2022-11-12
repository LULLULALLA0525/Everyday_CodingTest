def solution(n, p):
    p = sorted(p)
    sum_p = [sum(p[:i]) for i in range(1, n + 1)]
    return sum(sum_p)


N = int(input())
P = list(map(int, input().split()))
print(solution(N, P))
