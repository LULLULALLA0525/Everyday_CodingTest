import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, edges, costs):
  answer = 0 

  minCost = 1_000_000_000
  for i in range(n - 1):
    minCost = min(minCost, costs[i])
    answer += edges[i] * minCost

  return answer

N = int(input())
EDGES = list(map(int, input().split()))
COSTS = list(map(int, input().split()))
print(solution(N, EDGES, COSTS))