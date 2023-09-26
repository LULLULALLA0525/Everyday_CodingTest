import sys

input = lambda: sys.stdin.readline()

#     북  동  남  서
dx = [ 0, 1, 0, -1]
dy = [-1, 0, 1,  0]

def solution(n, m, y, x, d, room):
  result = 0
  while(True):
    if room[y][x] == 0:
      room[y][x] = 2
      result += 1

    moved = False
    for i in [(d + 3) % 4, (d + 2) % 4, (d + 1) % 4, d]:
      nx, ny = (x + dx[i]), (y + dy[i])
      if room[ny][nx] == 0:
        x, y = nx, ny
        d = i
        moved = True
        break

    if moved:
      continue
    else:
      nx, ny = (x + dx[(d + 2) % 4]), (y + dy[(d + 2) % 4])
      if room[ny][nx] == 1:
        break
      else:
        x, y = nx, ny

  return result

N, M = list(map(int, input().split()))
Y, X, D = list(map(int, input().split()))
ROOM = []
for _ in range(N):
  ROOM.append(list(map(int, input().split())))
print(solution(N, M, Y, X, D, ROOM))