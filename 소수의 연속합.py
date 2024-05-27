import sys

input = lambda: sys.stdin.readline()

def is_prime_number(n):
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def prime_numbers_less_than(n):
  result = set(range(2, n + 1))
  for i in range(2, n + 1):
    if i in result:
      result -= set(range(2*i, n + 1, i))
  return sorted(list(result))

def solution(n):
  if n == 1:
    return 0
  if n == 2:
    return 1

  answer = 0
  if is_prime_number(n):
    answer += 1

  prime_list = prime_numbers_less_than((n // 2) + 1)

  start, end = 0, 0
  value = prime_list[0]
  length = len(prime_list)
  while end < length:
    if value == n:
      answer += 1
      end += 1
      if end == length:
        break
      value += prime_list[end]

      if start == end:
        break
      value -= prime_list[start]
      start += 1

    elif value > n:
      if start == end:
        break
      value -= prime_list[start]
      start += 1

    elif value < n:
      end += 1
      if end == length:
        break
      value += prime_list[end]

  return answer

N = int(input())
print(solution(N))