import heapq
import sys

input = lambda: sys.stdin.readline()

# def solution(table):
#   result = 0

#   n = len(table)
#   numbers_position = [ [n - 1, i] for i in range(n) ]

#   for _ in range(n):
#     numbers = [ [table[row][col], row, col] for row, col in numbers_position ]
#     max_number = max(numbers, key=lambda x: x[0])
#     result = max_number[0]
#     row, col = max_number[1:]
    
#     numbers_position.remove([row, col])

#     if row - 1 >= 0:
#       numbers_position.append([row - 1, col])

#   return result

N = int(input())
# TABLE = [list(map(int, input().split())) for _ in range(N)]
# print(solution(TABLE))
TABLE = []
for _ in range(N):
  for number in list(map(int, input().split())):
    heapq.heappush(TABLE, number)
    if len(TABLE) > N:
      heapq.heappop(TABLE)
print(heapq.heappop(TABLE))