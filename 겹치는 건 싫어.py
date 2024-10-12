import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

def solution(n, k, numbers):
  count = defaultdict(int)

  start, end = 0, 0
  answer = 0
  while end < n:
    if count[numbers[end]] < k:
      count[numbers[end]] += 1
      answer = max(answer, end - start + 1)
      end += 1
    else:
      count[numbers[start]] -= 1
      start += 1

  return answer

N, K = list(map(int, input().split()))
NUMBERS = list(map(int, input().split()))
print(solution(N, K, NUMBERS))