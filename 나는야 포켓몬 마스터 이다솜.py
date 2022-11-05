import sys
input = sys.stdin.readline


def solution(n):
    if n.isdigit():
        return BIBLE_BY_NUM[int(n)]
    else:
        return BIBLE_BY_NAME[n]


N, K = list(map(int, input().split()))
BIBLE_BY_NUM = {}
BIBLE_BY_NAME = {}
for i in range(1, N + 1):
    name = input().split('\n')[0]
    BIBLE_BY_NAME[name] = i
    BIBLE_BY_NUM[i] = name
for _ in range(K):
    print(solution(input().split('\n')[0]))
