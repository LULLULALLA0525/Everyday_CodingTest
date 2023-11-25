import sys
from collections import Counter

input = lambda: sys.stdin.readline()

def solution(topping):
  result = 0
  left, right = Counter([]), Counter(topping)
  for i in range(len(topping) - 1):
    left[topping[i]] += 1
    right[topping[i]] -= 1
    
    if right[topping[i]] <= 0:
      del right[topping[i]]

    if len(left) == len(right):
      result += 1
  return result

TOPPING = list(map(int, input().split()))
print(solution(TOPPING))