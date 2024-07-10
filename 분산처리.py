import sys

input = lambda: sys.stdin.readline().rstrip()

# a^b의 1의 자릿수를 출력하는 함수
def getLastDigitAfterPower(a, b):
  # 거듭제곱은 4를 주기로 반복된다.
  result = a ** (b % 4 + 4) % 10
  if result == 0:
    return 10
  else:
    return result

T = int(input())
ANSWERS = []
for _ in range(T):
  A, B = list(map(int, input().split()))
  ANSWERS.append(getLastDigitAfterPower(A % 10, B))
for ANSWER in ANSWERS:
  print(ANSWER)