import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(game, players):
  if game == 'Y':
    return len(set(players))
  elif game == 'F':
    return len(set(players)) // 2
  else:
    return len(set(players)) // 3

N, GAME = list(input().split())
PLAYERS = []
for _ in range(int(N)):
  PLAYERS.append(input())
print(solution(GAME, PLAYERS))