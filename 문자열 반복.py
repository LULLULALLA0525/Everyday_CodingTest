import sys

input = lambda: sys.stdin.readline()

def solution(n, string):
  chars = list(string)

  result = ""
  for char in chars:
    result += char*n

  return result

T = int(input())
ANSWERS = []
for _ in range(T):
  N, STRING = list(input().split())
  ANSWERS.append(solution(int(N), STRING))

for ANSWER in ANSWERS:
  print(ANSWER)