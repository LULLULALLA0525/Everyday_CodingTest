import sys

input = lambda: sys.stdin.readline().rstrip()

BOY, GIRL = 1, 2
ON, OFF = '1', '0'

def toggle(state):
  if state == ON:
    return OFF
  else:
    return ON

def solution(switches, students):
  for gender, switch in students:
    if gender == BOY:
      index = switch - 1
      while index < len(switches):
        switches[index] = toggle(switches[index])
        index += switch
    else:
      switches[switch - 1] = toggle(switches[switch - 1])
      if switch >= (len(switches) // 2) + 1:
        for end in range(switch, len(switches)):
          start = ((switch - 1) * 2) - end
          if switches[start] == switches[end]:
            switches[start] = toggle(switches[start])
            switches[end] = toggle(switches[end])
          else:
            break
      else:
        for start in range(switch - 2, -1, -1):
          end = ((switch - 1) * 2) - start
          if switches[start] == switches[end]:
            switches[start] = toggle(switches[start])
            switches[end] = toggle(switches[end])
          else:
            break

  return switches

N_SWITCH = int(input())
SWITCHES = list(input().split())
N_STUDENT = int(input())
STUDENTS = []
for _ in range(N_STUDENT):
  STUDENTS.append(list(map(int, input().split())))
RESULT = solution(SWITCHES, STUDENTS)
if N_SWITCH <= 20:
  print(' '.join(RESULT))
elif N_SWITCH <= 40:
  print(' '.join(RESULT[:20]))
  print(' '.join(RESULT[20:]))
elif N_SWITCH <= 60:
  print(' '.join(RESULT[:20]))
  print(' '.join(RESULT[20:40]))
  print(' '.join(RESULT[40:]))
elif N_SWITCH <= 80:
  print(' '.join(RESULT[:20]))
  print(' '.join(RESULT[20:40]))
  print(' '.join(RESULT[40:60]))
  print(' '.join(RESULT[60:]))
else:
  print(' '.join(RESULT[:20]))
  print(' '.join(RESULT[20:40]))
  print(' '.join(RESULT[40:60]))
  print(' '.join(RESULT[60:80]))
  print(' '.join(RESULT[80:]))