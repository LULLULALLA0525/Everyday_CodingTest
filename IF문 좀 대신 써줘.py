import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline()

def solution(tiers, players):
  tiers_score = list(map(lambda x: x[1], tiers))
  for player in players:
    index = bisect_left(tiers_score, player)
    print(tiers[index][0])

N, M = list(map(int, input().split()))
TIERS = []
for _ in range(N):
  name, power = list(input().split())
  TIERS.append([name, int(power)]) 
PLAYERS = [int(input()) for _ in range(M)]

solution(TIERS, PLAYERS)