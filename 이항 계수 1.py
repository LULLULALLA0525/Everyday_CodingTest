def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def solution(n, k):
    large = max([n, k])
    small = min([n, k])

    value = 1
    for i in range(small):
        value *= (large - i)
    fact = factorial(small)
    return value // fact


N, K = list(map(int, input().split()))
print(solution(N, K))
