import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

def solution(n, balls):
  leftBall, rightBall = balls[0], balls[-1]

  leftGroup = 0
  for index in range(n):
    if balls[index] == leftBall:
      leftGroup += 1
    else:
      break

  rightGroup = 0
  for index in range(n - 1, -1, -1):
    if balls[index] == rightBall:
      rightGroup += 1
    else:
      break
  
  count = Counter(balls)
  
  return min(count['B'], count['R'], count[leftBall] - leftGroup, count[rightBall] - rightGroup)

N = int(input())
BALLS = list(input())
print(solution(N, BALLS))