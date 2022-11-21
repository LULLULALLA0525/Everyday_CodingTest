import sys

input = lambda: sys.stdin.readline()


def solution(wear):
    wears = {}
    for i in range(len(wear)):
        if wear[i][1] not in wears.keys():
            wears[wear[i][1]] = [""]
        wears[wear[i][1]].append(wear[i][0])
    answer = 1
    for k in wears.keys():
        answer *= len(wears[k])
    return answer - 1


T = int(input())
for _ in range(T):
    N = int(input())
    WEAR = []
    for _ in range(N):
        WEAR.append(list(input().split()))
    print(solution(WEAR))
