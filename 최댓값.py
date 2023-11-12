import sys

input = lambda: sys.stdin.readline()

def solution(numbers):
  print(max(numbers))
  print(numbers.index(max(numbers)) + 1)

NUMBERS = [int(input()) for _ in range(9)]
solution(NUMBERS)