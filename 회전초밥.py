import sys
from queue import deque

input = lambda: sys.stdin.readline()

def solution(k, c, sushies):
  result = 0

  sub_list = deque(sushies[:k])
  length = len(set(list(sub_list) + [c]))

  result = max(result, length)

  for i in range(len(sushies)):
    sub_list.popleft()
    sub_list.append(sushies[(i + k + 1) % len(sushies)])

    length = len(set(list(sub_list) + [c]))

    result = max(result, length)

  return result

N, D, K, C = list(map(int, input().split()))
SUSHIES = [int(input()) for _ in range(N)]
print(solution(K, C, SUSHIES))