import sys

input = lambda: sys.stdin.readline()

def solution(numbers):
  max_num = max(numbers)
  result = 0
  for start in range(len(numbers)):
    isShown = [False for _ in range(max_num + 1)]
    for end in range(start, len(numbers)):
      if isShown[numbers[end]]:
        break
      else:
        result += 1
        isShown[numbers[end]] = True

  return result

N = int(input())
NUMBERS = list(map(int, input().split()))
print(solution(NUMBERS))