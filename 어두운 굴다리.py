import sys

input = lambda: sys.stdin.readline()

def solution(n, lights):
  gap = []
  for i in range(len(lights) - 1):
    if i == 0:
      gap.append(lights[i])
    else:
      gap.append((lights[i+1] - lights[i] + 1)//2)
  gap.append(n - lights[-1])
  
  return max(gap)

N = int(input())
M = int(input())
LIGHTS = list(map(int, input().split()))
print(solution(N, LIGHTS))