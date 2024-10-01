import sys

input = lambda: sys.stdin.readline().rstrip()

MOVE_DOWN, MOVE_UP, SWITCH_DOWN, SWITCH_UP = '1', '2', '3', '4'

def solution(channels):
  answer = ''

  KBS1_index = -1
  KBS2_index = -1
  for index, value in enumerate(channels):
    if value == 'KBS1':
      KBS1_index = index
    elif value == 'KBS2':
      KBS2_index = index
    
    if KBS1_index != -1 and KBS2_index != -1:
      break
  
  answer += MOVE_DOWN * KBS1_index
  answer += SWITCH_UP * KBS1_index

  if KBS1_index > KBS2_index:
    KBS2_index += 1
  answer += MOVE_DOWN * KBS2_index
  answer += SWITCH_UP * (KBS2_index - 1)

  return answer

N = int(input())
CHANNELS = []
for _ in range(N):
  CHANNELS.append(input())
print(solution(CHANNELS))