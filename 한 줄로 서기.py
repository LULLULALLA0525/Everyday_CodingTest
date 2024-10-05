import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, memories):
  answer = [ "." for _ in range(n) ]
  remain = list(range(n))

  for index, memory in enumerate(memories):
    height = index + 1
    order = remain.pop(memory)
    answer[order] = str(height)

  return ' '.join(answer)

N = int(input())
MEMORIES = list(map(int, input().split()))
print(solution(N, MEMORIES))