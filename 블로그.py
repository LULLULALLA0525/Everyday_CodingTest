import sys

input = lambda: sys.stdin.readline()

def solution(x, users):
  result = [sum(users[:x])]
  prev_sum = sum(users[1:x])
  for i in range(1, len(users) - x + 1):
    max_value = result[0]
    cur_sum = prev_sum + users[x + i - 1]
    if cur_sum > max_value:
      result = [cur_sum]
    elif cur_sum >= max_value:
      result.append(cur_sum)
    prev_sum = cur_sum - users[i]

  if result[0] == 0:
    print("SAD")
  else:
    print(result[0])
    print(len(result))

N, X = list(map(int, input().split()))
USERS = list(map(int, input().split()))
solution(X, USERS)