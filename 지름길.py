import sys

input = lambda: sys.stdin.readline()

START, END, DISTANCE = 0, 1, 2

def solution(d, paths):
  distance = [i for i in range(d + 1)]

  for i in range(1, len(distance)):
    shortcut = i
    for path in paths:
      if i == path[END]:
        shortcut = min(shortcut, distance[path[START]] + path[DISTANCE])
    distance[i] = min(distance[i], distance[i - 1] + 1, shortcut)

  return distance[-1]

N, D = list(map(int, input().split()))
PATHS = []
for _ in range(N):
  PATHS.append(list(map(int, input().split())))
print(solution(D, PATHS))