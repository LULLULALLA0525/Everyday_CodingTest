import sys

input = lambda: sys.stdin.readline()

def solution(names):
  names_length_3 = filter(lambda name: len(name) == 3, names)
  return min(names_length_3)

N = int(input())
NAMES = [input().strip() for _ in range(N)]
print(solution(NAMES))