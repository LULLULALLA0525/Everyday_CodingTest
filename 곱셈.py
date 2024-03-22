import sys

input = lambda: sys.stdin.readline()

def solution(a, b, c):
  if b == 1:
    return a % c
  else:
    x = solution(a, b//2, c)
    if b & 1:
      return (x*x*(a%c))%c
    else:
      return (x*x)%c

A, B, C = list(map(int, input().split()))
result = solution(A, B, C)
print(result)