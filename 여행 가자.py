import sys
from collections import deque

input = lambda: sys.stdin.readline()

def solution(cities, plan):
  plan = list(set(plan))
  start = plan[0]
  reachable_cities = [False for _ in range(len(cities))]

  queue = deque()
  queue.append(start)
  while(queue):
    cur = queue.popleft()
    reachable_cities[cur] = True
    
    direct_cities = list(filter(lambda city: cities[cur][city] == 1 and not reachable_cities[city], range(len(cities))))
    for city in direct_cities:
      queue.append(city)
  
  for city in plan:
    if not reachable_cities[city]:
      return "NO"

  return "YES"

N = int(input())
M = int(input())
CITIES = [list(map(int, input().split())) for _ in range(N)]
PLAN = list(map(lambda x: int(x) - 1, input().split()))
print(solution(CITIES, PLAN))