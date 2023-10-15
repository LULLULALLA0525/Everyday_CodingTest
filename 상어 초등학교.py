import sys

input = lambda: sys.stdin.readline()

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
def analyze_seat(seats, x, y, like):
  empty, friends = 0, 0
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or ny < 0 or nx >= len(seats) or ny >= len(seats):
      continue
    elif seats[ny][nx] == 0:
      empty += 1
    elif seats[ny][nx] in like:
      friends += 1
    else:
      continue
  return empty, friends

def solution(n, order, likes):
  seats = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(len(order)):
    student = order[i]

    empty_seats = []
    for y in range(n):
      for x in range(n):
        if seats[y][x] == 0:
          empty, friends = analyze_seat(seats, x, y, likes[student])
          empty_seats.append([x, y, empty, friends])
    
    selected_seat = sorted(empty_seats, key = lambda x: (-x[3], -x[2], x[1], x[0]))[0]
    x, y = selected_seat[:2]
    seats[y][x] = student

  result = 0
  for y in range(n):
    for x in range(n):
      student = seats[y][x]
      _, friends = analyze_seat(seats, x, y, likes[student])
      if friends == 0:
        result += 0
      elif friends == 1:
        result += 1
      elif friends == 2:
        result += 10
      elif friends == 3:
        result += 100
      elif friends == 4:
        result += 1000
    
  return result

N = int(input())
ORDER = []
LIKES = [[] for _ in range(N**2 + 1)]
for _ in range(N**2):
  student, one, two, three, four = list(map(int, input().split()))
  ORDER.append(student)
  LIKES[student] = [one, two, three, four]

print(solution(N, ORDER, LIKES))