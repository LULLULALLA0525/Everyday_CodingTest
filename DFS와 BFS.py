import sys
from collections import deque

input = lambda: sys.stdin.readline()


def dfs(graph, dfs_visited, start):
    dfs_visited[start] = True
    print(start, end=" ")
    for nxt in graph[start]:
        if not dfs_visited[nxt]:
            dfs(graph, dfs_visited, nxt)


def bfs(graph, start):
    result = []
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        if not visited[cur]:
            visited[cur] = True
            result.append(cur)
            for nxt in graph[cur]:
                if not visited[nxt]:
                    queue.append(nxt)
    for i in range(len(result)):
        print(result[i], end=" ")


N, M, V = list(map(int, input().split()))
GRAPH = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = list(map(int, input().split()))
    GRAPH[A].append(B)
    GRAPH[B].append(A)
for g in range(len(GRAPH)):
    GRAPH[g] = sorted(GRAPH[g])

VISIT = [False] * (N + 1)
dfs(GRAPH, VISIT, V)
print()
bfs(GRAPH, V)
