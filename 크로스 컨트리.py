import sys
from collections import Counter, defaultdict

input = lambda: sys.stdin.readline().rstrip()

def solution(teams):
  counter = Counter(teams)

  team_score = defaultdict(list)
  current = 1
  for team in teams:
    if counter[team] >= 6:
      team_score[team].append(current)
      current += 1
    
  team_rank = []
  for team in team_score.keys():
    score = sum(team_score[team][:4])
    fifth = team_score[team][4]
    team_rank.append([score, fifth, team])

  return sorted(team_rank)[0][2]

T = int(input())
ANSWERS = []
for _ in range(T):
  N = int(input())
  TEAMS = list(map(int, input().split()))
  ANSWERS.append(solution(TEAMS))

for ANSWER in ANSWERS:
  print(ANSWER)