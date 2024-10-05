import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

INDEX, HEIGHT = 0, 1

def solution(walls):
  columns = defaultdict(int)
  tallestWall = [0, 0]
  farthestWall = [0, 0]
  for index, height in walls:
    columns[index] = height
    if index >= farthestWall[INDEX]:
      farthestWall = [index, height]
    if height >= tallestWall[HEIGHT]:
      tallestWall = [index, height]

  answer = 0
  ceiling = 0
  for index in range(tallestWall[INDEX]):
    if columns[index] > ceiling:
      ceiling = columns[index]
    answer += ceiling
  answer += tallestWall[HEIGHT]
  ceiling = 0
  for index in range(farthestWall[INDEX], tallestWall[INDEX], -1):
    if columns[index] > ceiling:
      ceiling = columns[index]
    answer += ceiling

  return answer

N = int(input())
WALLS = []
for _ in range(N):
  WALLS.append(list(map(int, input().split())))
print(solution(WALLS))