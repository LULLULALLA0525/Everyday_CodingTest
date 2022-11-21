import sys

input = lambda: sys.stdin.readline()


def solution(s, n):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for c in s:
        if c in alpha:
            next_idx = (alpha.index(c) + n) % 52
            result.append(alpha[next_idx])
        else:
            next_val = int(c) + n
            result.append(str(next_val))

    answer = ''.join(result)
    return answer


S = input().strip()
N = int(input())
print(solution(S, N))
