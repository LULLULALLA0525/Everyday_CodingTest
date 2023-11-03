import sys

input = lambda: sys.stdin.readline()

def solution(string, k):
  alpha = dict()
  for i in range(len(string)):
    if string[i] in alpha:
      alpha[string[i]].append(i)
    else:
      alpha[string[i]] = [i]

  min_length = 10001
  max_length = 0
  for key in alpha:
    if len(alpha[key]) >= k:
      for i in range(len(alpha[key]) - k + 1):
        length = alpha[key][i + k - 1] - alpha[key][i] + 1
        min_length = min(min_length, length)
        max_length = max(max_length, length)
    
  if min_length == 10001 and max_length == 0:
    print("-1")
  else:
    print(min_length, max_length)

T = int(input())
for _ in range(T):
  STRING = input().strip()
  K = int(input())
  solution(STRING, K)