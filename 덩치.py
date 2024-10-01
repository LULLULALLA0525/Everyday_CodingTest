import sys

input = lambda: sys.stdin.readline().rstrip()

INDEX, WEIGHT, HEIGHT = 0, 1, 2

def solution(measurements):
  answer = []

  for measure in measurements:
    heavy = []
    tall = []
    for comp in measurements:
      if comp[WEIGHT] > measure[WEIGHT]:
        heavy.append(comp[INDEX])
      if comp[HEIGHT] > measure[HEIGHT]:
        tall.append(comp[INDEX])
    answer.append(len(set(heavy) & set(tall)) + 1)

  return ' '.join(map(str, answer))

N = int(input())
MEASUREMENTS = []
for I in range(N):
  W, H = list(map(int, input().split()))
  MEASUREMENTS.append([I, W, H])
print(solution(MEASUREMENTS))