import sys
from bisect import bisect_left, insort

input = lambda: sys.stdin.readline().rstrip()

def solution(children):
  answer = 0

  line = []
  for child in children:
    answer += len(line) - bisect_left(line, child)
    insort(line, child)

  return answer

P = int(input())
CASES = []
for _ in range(P):
  CHILDREN = list(map(int, input().split()))
  RESULT = solution(CHILDREN[1:])
  CASES.append(RESULT)
for INDEX in range(P):
  print(INDEX + 1, end=' ')
  print(CASES[INDEX])