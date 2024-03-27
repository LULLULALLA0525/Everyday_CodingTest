import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline()

def solution(n, s, array):
  answer = n + 1

  sum_array = [0]
  for i in range(n):
    sum_array.append(array[i] + sum_array[i])

  small, big = 0, bisect_left(sum_array, s)
  while big <= n:
    if big > small and sum_array[big] - sum_array[small] >= s:
      answer = min(answer, big-small)
      small += 1
    else:
      big += 1

  if answer == n + 1:
    return 0
  else:
    return answer

N, S = list(map(int, input().split()))
ARRAY = list(map(int, input().split()))
print(solution(N, S, ARRAY))