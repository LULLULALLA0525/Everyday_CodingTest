import sys
from itertools import permutations

input = lambda: sys.stdin.readline()

def solution(durations, problems):
  result = 7001
  plans = list(permutations(range(len(problems))))

  for plan in plans:  # 반복 횟수 최대 7!(5,040)
    learn = 0
    knowledges = [[] for _ in range(len(plan))]  # 각 인덱스의 리스트는 해당 날에 기억하는 지식의 종류
    for day in range(len(plan)):  # 반복 횟수 최대 7
      problem = problems[plan[day]]
      knowledges_to_learn = list(set(problem) - set(knowledges[day]))
      learn += len(knowledges_to_learn)

      if learn >= result:
        break

      for knowledge in knowledges_to_learn:   # 반복 횟수 최대 1,000
        for date in range(day, min(day + durations[knowledge], len(plan))):   # 반복 횟수 최대 7
          knowledges[date].append(knowledge)

    result = min(learn, result)

  return result

N, M = list(map(int, input().split()))
DURATIONS = [0] + list(map(int, input().split()))
PROBLEMS = [list(map(int, input().split()))[1:] for _ in range(M)]
print(solution(DURATIONS, PROBLEMS))