import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n):
  if n % 2 == 0:
    return 'CY'
  else:
    return 'SK'

N = int(input())
print(solution(N))