import heapq
import sys

input = lambda: sys.stdin.readline()

N = int(input())
numbers = []
for _ in range(N):
  number = int(input())
  if number == 0:
    if len(numbers) == 0:
      print(0)
    else:
      print(heapq.heappop(numbers))
  else:
    heapq.heappush(numbers, number)