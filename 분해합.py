def constructor(a):
    s = str(a)
    result = a
    for i in range(len(s)):
        result += int(s[i])
    return result


def solution(n):
    for i in range(n):
        if n == constructor(i):
            return i
    return 0


n = int(input())
print(solution(n))
