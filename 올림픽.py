import sys

input = lambda: sys.stdin.readline().rstrip()

NUMBER, GOLD, SILVER, BRONZE = 0, 1, 2, 3

def solution(k, medals):
  gold, silver, bronze = 0, 0, 0
  for medal in medals:
    if medal[NUMBER] == k:
      gold, silver, bronze = medal[1:]

  sortedList = sorted(medals, key=lambda medal: (-medal[GOLD], -medal[SILVER], -medal[BRONZE]))

  for i in range(len(sortedList)):
    if sortedList[i][1:] == [gold, silver, bronze]:
      return i + 1

N, K = list(map(int, input().split()))
MEDALS = []
for _ in range(N):
  MEDAL = list(map(int, input().split()))
  MEDALS.append(MEDAL)
print(solution(K, MEDALS))