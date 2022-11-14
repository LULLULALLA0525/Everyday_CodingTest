import sys
from collections import deque

input = lambda: sys.stdin.readline()


def solution(n, graph):
    answer = 0
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(1)
    while queue:
        cur = queue.popleft()
        if visited[cur]:
            continue
        else:
            visited[cur] = True
            answer += 1
            for node in graph[cur]:
                queue.append(node)
    return answer - 1


N = int(input())
K = int(input())
GRAPH = [[] for _ in range(N + 1)]
for _ in range(K):
    a, b = list(map(int, input().split()))
    GRAPH[a].append(b)
    GRAPH[b].append(a)
print(solution(N, GRAPH))
