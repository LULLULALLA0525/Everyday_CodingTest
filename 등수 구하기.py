import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()

def solution(leaderboard, p, score):
  if len(leaderboard) == p:
    if score <= leaderboard[-1]:
      return -1

  index = bisect_left(list(map(lambda x: -x, leaderboard)), -score) + 1

  return index

N, SCORE, P = list(map(int, input().split()))
LEADERBOARD = list(map(int, input().split()))
print(solution(LEADERBOARD, P, SCORE))