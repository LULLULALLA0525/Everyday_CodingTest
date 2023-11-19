import heapq
import sys

input = lambda: sys.stdin.readline()

MONSTER, ITEM = 1, 2
TYPE, DEAL= 0, 1

def solution(n, d, initial_rooms):
  rooms = [[], [], []]
  for room in initial_rooms:
    heapq.heappush(rooms[room[TYPE]], room[DEAL])

  result = 0
  while rooms[MONSTER]:
    monster = heapq.heappop(rooms[MONSTER])
    if d > monster:
      d += monster
      result += 1
    elif rooms[ITEM]:
      heapq.heappush(rooms[MONSTER], monster)
      d *= heapq.heappop(rooms[ITEM])
      result += 1
    else:
      return result
  
  return n

N, D = list(map(int, input().split()))
ROOMS = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, D, ROOMS))