def solution(S):
    a = 'abcdefghijklmnopqrstuvwxyz'
    alpha = {}
    for i in range(26):
        alpha[a[i]] = i + 1

    h = [alpha[s] for s in S]
    result = 0
    hashing = 1
    for i in range(len(h)):
        result += h[i] * hashing
        hashing *= 31

    return result % 1234567891


L = int(input())
S = list(input())
print(solution(S))
