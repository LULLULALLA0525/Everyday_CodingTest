import sys
from collections import defaultdict

input = sys.stdin.readline
print = sys.stdout.write

dp = defaultdict(lambda: 0)

def solution(time, graph, building):
  if dp[building] != 0:
    return dp[building]

  max_time = 0
  for prev in graph[building]:
    max_time = max(max_time, solution(time, graph, prev))
  
  dp[building] = max_time + time[building]
  return dp[building]

ANSWERS = []
T = int(input())
for _ in range(T):
  dp = defaultdict(lambda: 0)
  N, K = list(map(int, input().split()))
  TIME = [0] + list(map(int, input().split()))
  GRAPH = defaultdict(list)
  for _ in range(K):
    FIRST, SECOND = list(map(int, input().split()))
    GRAPH[SECOND].append(FIRST)
  BUILDING = int(input())
  ANSWERS.append(solution(TIME, GRAPH, BUILDING))
for ANSWER in ANSWERS:
  print(str(ANSWER) + "\n")