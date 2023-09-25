import sys
from itertools import combinations

input = lambda: sys.stdin.readline()

def solution(table):
  simplified_table = [[table[i][j] + table[j][i] for i in range(len(table))] for j in range(len(table))]
  members = [i for i in range(len(table))]

  cases = map(
    lambda team1: [list(team1), list(filter(lambda member: member not in team1, members))],
    combinations(members, len(table) // 2)
  )
  
  results = []
  for case in cases:
    team1 = sum(
      map(
        lambda pair: simplified_table[pair[0]][pair[1]],
        combinations(case[0], 2)
      )
    )
    team2 = sum(
      map(
        lambda pair: simplified_table[pair[0]][pair[1]],
        combinations(case[1], 2)
      )
    )
    results.append(abs(team1 - team2))

  return min(results)

N = int(input())
TABLE = []
for _ in range(N):
  TABLE.append(list(map(int, input().split())))
print(solution(TABLE))