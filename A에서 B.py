import sys

input = lambda: sys.stdin.readline()

def solution(a, b):
  count = 1
  while b > a:
    count += 1
    if b % 10 == 1:
      b //= 10
    elif b % 2 == 0:
      b //= 2
    else:
      return -1
  
  if b == a:
    return count
  else:
    return -1

A, B = list(map(int, input().split()))
print(solution(A, B))