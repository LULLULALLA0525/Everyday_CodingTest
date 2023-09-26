import sys

input = lambda: sys.stdin.readline()

RIGHT = 1   # 시계방향
LEFT = -1   # 반시계방향

def rotate_gear(gear, direction):
  if direction == RIGHT:
    rotated_gear = [gear[7]]
    for i in range(7):
      rotated_gear.append(gear[i])
    return rotated_gear
  elif direction == LEFT:
    rotated_gear = []
    for i in range(1, 8):
      rotated_gear.append(gear[i])
    rotated_gear.append(gear[0])
    return rotated_gear
  else:
    return gear

# 맞닿아 있는 톱니 종류
#   [0][2]-[1][6]
#   [1][2]-[2][6]
#   [2][2]-[3][6]
def solution(gears, rotates):
  for rotate in rotates:
    joints = [gears[i][2] != gears[i + 1][6] for i in range(3)]
    rotate_by_gear = [[i, 0] for i in range(4)]

    rotate_by_gear[rotate[0] - 1] = rotate[1]
    if rotate[0] - 1 == 0:  # 1번 기어가 회전
      if joints[0]: # 1, 2번 기어가 맞물린 경우
        rotate_by_gear[1] = -rotate[1]
        if joints[1]: # 2, 3번 기어가 맞물린 경우
          rotate_by_gear[2] = rotate[1]
          if joints[2]: # 3, 4번 기어가 맞물린 경우
            rotate_by_gear[3] = -rotate[1]
    elif rotate[0] - 1 == 1:  # 2번 기어가 회전
      if joints[0]: # 1, 2번 기어가 맞물린 경우
        rotate_by_gear[0] = -rotate[1]
      if joints[1]: # 2, 3번 기어가 맞물린 경우
        rotate_by_gear[2] = -rotate[1]
        if joints[2]: # 3, 4번 기어가 맞물린 경우
          rotate_by_gear[3] = rotate[1]
    elif rotate[0] - 1 == 2:  # 3번 기어가 회전
      if joints[1]: # 2, 3번 기어가 맞물린 경우
        rotate_by_gear[1] = -rotate[1]
        if joints[0]: # 1, 2번 기어가 맞물린 경우
          rotate_by_gear[0] = rotate[1]
      if joints[2]: # 3, 4번 기어가 맞물린 경우
        rotate_by_gear[3] = -rotate[1]
    else: # 4번 기어가 회전
      if joints[2]: # 3, 4번 기어가 맞물린 경우
        rotate_by_gear[2] = -rotate[1]
        if joints[1]: # 2, 3번 기어가 맞물린 경우
          rotate_by_gear[1] = rotate[1]
          if joints[0]: # 3, 4번 기어가 맞물린 경우
            rotate_by_gear[0] = -rotate[1]

    for i in range(len(gears)):
      gears[i] = rotate_gear(gears[i], rotate_by_gear[i])

  result = 0
  for i in range(len(gears)):
    if gears[i][0] == 1:
      result += 2**i

  return result

GEARS = []
for _ in range(4):
  GEARS.append(list(map(int, list(input().strip()))))
K = int(input())
ROTATES = []
for _ in range(K):
  # [0]은 GEAR 인덱스 + 1, [1]은 회전 방향
  ROTATES.append(list(map(int, input().split())))

print(solution(GEARS, ROTATES))