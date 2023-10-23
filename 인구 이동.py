import sys
from collections import deque

input = lambda: sys.stdin.readline()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(countries, l, r):
  count = 0
  while(True):
    moved, union_num = 0, 0
    union = [ [ union_num for _ in range(len(countries)) ] for _ in range(len(countries)) ]

    for row in range(len(countries)):
      for col in range(len(countries)):
        if union[row][col] == 0:
          union_num += 1
          countries_of_union = []
          sum_of_people = 0
          
          queue = deque()
          queue.append([row, col])
          while(queue):
            y, x = queue.popleft()

            if union[y][x] == 0:
              union[y][x] = union_num
              countries_of_union.append([y, x])
              sum_of_people += countries[y][x]

              for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(countries) or ny >= len(countries):
                  continue
                if union[ny][nx] == 0:
                  gap = abs(countries[ny][nx] - countries[y][x])
                  if l <= gap and gap <= r:
                    queue.append([ny, nx])

          if len(countries_of_union) > 1:
            moved += 1
            for country in countries_of_union:
              y, x = country
              countries[y][x] = sum_of_people // len(countries_of_union)

    if moved == 0:
      break
    else:
      count += 1

  return count

N, L, R = list(map(int, input().split()))
COUNTRIES = []
for _ in range(N):
  COUNTRIES.append(list(map(int, input().split())))
print(solution(COUNTRIES, L, R))