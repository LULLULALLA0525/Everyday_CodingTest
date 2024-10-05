import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solution(string, commands):
  left = deque(string)
  right = deque()

  for command in commands:
    if command[0] == 'L':
      if len(left) > 0:
        right.appendleft(left.pop())
    elif command[0] == 'D':
      if len(right) > 0:
        left.append(right.popleft())
    elif command[0] == 'B':
      if len(left) > 0:
        left.pop()
    elif command[0] == 'P':
      char = command[1]
      left.append(char)

  return ''.join(left) + ''.join(right)

STR = list(input())
M = int(input())
COMMANDS = []
for _ in range(M):
  COMMANDS.append(list(input().split()))
print(solution(STR, COMMANDS))