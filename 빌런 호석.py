import sys
from itertools import product

input = lambda: sys.stdin.readline()

swap = [
  [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
  [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
  [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
  [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
  [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
  [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
  [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
  [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
  [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
  [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

def solution(n, k, p, x):
  digits = [x % 10**(k - i) // 10**(k - i - 1) for i in range(k)]

  cases = list(map(list, product(list(range(8)), repeat = k)))
  valid_cases = list(filter(lambda case: sum(case) <= p, cases))

  result = []
  for case in valid_cases:
    available = True
    valid_changes = []
    for index in range(k):
      change = list(filter(lambda num: swap[digits[index]][num] == case[index], range(10)))
      if len(change) == 0:
        available = False
        break
      
      valid_changes.append(change)

    if not available:
      continue

    if len(valid_changes) > 0:
      numbers = list(map(lambda num: int(''.join(map(str, list(num)))), product(*valid_changes)))
      valid_numbers = list(filter(lambda number: number <= n, numbers))
      result += valid_numbers

  result = list(set(result))  # 중복 제거
  result.remove(x)            # 자기자신 제외
  if 0 in result:
    result.remove(0)          # 0층 제외
  return len(result)

N, K, P, X = list(map(int, input().split()))
print(solution(N, K, P, X))