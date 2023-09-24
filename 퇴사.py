import sys

input = lambda: sys.stdin.readline()


def solution(schedules):
  result = [0 for _ in range(len(schedules))]
  for i in range(len(schedules) - 1, -1, -1):
    if i + schedules[i][0] < len(schedules):
      result[i] = max(schedules[i][1] + result[i + schedules[i][0]], max(result[i:]))
    elif i + schedules[i][0] == len(schedules):
      result[i] = max(schedules[i][1], max(result[i:]))
    else:
      result[i] = max(result[i:])

  return result


DAYS = int(input())
SCHEDULES = []
for _ in range(DAYS):
  SCHEDULES.append(list(map(int, input().split())))
print(solution(SCHEDULES))
