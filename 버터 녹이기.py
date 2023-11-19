import sys

input = lambda: sys.stdin.readline()

POSITION, HEIGHT = 0, 1

def solution(butters):
  butters = sorted(butters, key=lambda butter: butter[POSITION])

  result = 10**100
  for i in range(len(butters) - 1):
    left, right = butters[i], butters[i+1]
    distance = right[POSITION] - left[POSITION] - 1

    left_melt = (left[HEIGHT] - 1) // 2
    right_melt = (right[HEIGHT] - 1) // 2

    if left_melt + right_melt > distance:
      # 만난다!
      center = distance // 2
      if min(left_melt, right_melt) <= center:
        # 둘 중에 하나는 도달하지 못하는 경우
        result = min(result, distance - min(left_melt, right_melt))
      else:
        # 둘 다 도달하는 경우
        result = min(result, center)
    else:
      continue

  if result == 10**100:
    return "forever"
  
  return result

N = int(input())
BUTTERS = [list(map(int, input().split())) for _ in range(N)]
print(solution(BUTTERS))