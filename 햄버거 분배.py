import sys

input = lambda: sys.stdin.readline()

def solution(table, k):
  result = 0
  for i in range(len(table)):
    if table[i] == "P":
      if i < k:
        start = 0
      else:
        start = i - k

      if i + k >= len(table):
        end = len(table) - 1
      else:
        end = i + k

      for j in range(start, end + 1):
        if table[j] == "H":
          result += 1
          table[j] = "X"
          break

  return result

N, K = list(map(int, input().split()))
TABLE = list(input().strip())
print(solution(TABLE, K))