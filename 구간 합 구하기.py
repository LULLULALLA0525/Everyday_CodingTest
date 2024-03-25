import sys

input = lambda: sys.stdin.readline()

n, m = list(map(int, input().split()))
table = []
for _ in range(n):
  table.append(list(map(int, input().split())))

sum_table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for row in range(1, n + 1):
  for col in range(1, n + 1):
    if row == 0 and col == 0:
      sum_table[row][col] = table[row - 1][col - 1]
    elif row == 0:
      sum_table[row][col] = sum_table[row][col - 1] + table[row - 1][col - 1]
    elif col == 0:
      sum_table[row][col] = sum_table[row - 1][col] + table[row - 1][col - 1]
    else:
      sum_table[row][col] = sum_table[row - 1][col] + sum_table[row][col - 1] - sum_table[row - 1][col - 1] + table[row - 1][col - 1]

answers = []
for _ in range(m):
  x1, y1, x2, y2 = list(map(int, input().split()))

  answer = sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1]
  answers.append(answer)

for answer in answers:
  print(answer)