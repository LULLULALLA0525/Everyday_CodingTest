def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def solution(n):
    result = factorial(n)
    cnt = 0
    while result % 10 == 0:
        cnt += 1
        result //= 10

    return cnt


n = int(input())
print(solution(n))
