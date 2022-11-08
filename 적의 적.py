import sys

input = lambda: sys.stdin.readline()

def set_enemy(info, a, b):
    if b in info[a][ENEMY]:

    elif b in info[a][FRIEND]:
        return [0]
    else:
        info[a][DEFAULT].remove(b)
        info[]


DEFAULT = 0
ENEMY = 1
FRIEND = 2
def solution(n, rivals):
    info = []
    for _ in range(n):
        info.append([[j for j in range(1, n + 1)], [], []])

    for i in range(len(rivals)):

    return n


N, M = list(map(int, input().split()))
RIVALS = []
for _ in range(M):
    RIVALS.append(list(map(int, input())))
print(solution(N, RIVALS))
