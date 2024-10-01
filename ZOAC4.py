import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(h, w, n, m):
  column = h // (n + 1)
  if h % (n + 1) != 0:
    column += 1
  
  row = w // (m + 1)
  if w % (m + 1) != 0:
    row += 1

  return column*row

H, W, N, M = list(map(int, input().split()))
print(solution(H, W, N, M))