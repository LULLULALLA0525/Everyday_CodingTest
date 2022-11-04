def solution(n):
    num = 1
    i = 0
    while num < n:
        i += 1
        num += 6*i

    return i + 1


n = int(input())
print(solution(n))
