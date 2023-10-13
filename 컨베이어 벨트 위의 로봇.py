import sys

input = lambda: sys.stdin.readline()

def solution(n, k, rails):
  hasRobot = [False for _ in range(n*2)]
  
  result = 0
  while len(list(filter(lambda x: x == 0, rails))) < k:
    result += 1

    rails = [rails[-1]] + rails[:(n*2)-1]
    hasRobot = [hasRobot[-1]] + hasRobot[:(n*2)-1]
    
    for i in range(n-1, -1, -1):
      if hasRobot[i]:
        if i == n - 1:
          hasRobot[i] = False
        elif i == n - 2:
          if rails[i + 1] != 0:
            hasRobot[i] = False
            rails[i + 1] -= 1
        else:
          if rails[i + 1] != 0 and not hasRobot[i + 1]:
            hasRobot[i] = False
            hasRobot[i + 1] = True
            rails[i + 1] -= 1

    if rails[0] != 0:
      hasRobot[0] = True
      rails[0] -= 1

  return result

N, K = list(map(int, input().split()))
RAILS = list(map(int, input().split()))
print(solution(N, K, RAILS))