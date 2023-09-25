import sys
from functools import reduce
from itertools import product

input = lambda: sys.stdin.readline()

def calculate(acc, val, case):
  if case[val[0] - 1] == '+':
    return acc + val[1]
  elif case[val[0] - 1] == '-':
    return acc - val[1]
  elif case[val[0] - 1] == '*':
    return acc * val[1]
  else:
    if acc < 0 and val[1] > 0:
      return -((-acc)// val[1])
    else:
      return acc // val[1]

def solution(array, plus, minus, multiple, divide):
  cases = filter(
    lambda i: i.count('+') == plus and i.count('-') == minus and i.count('*') == multiple and i.count('//') == divide, 
    product(['+', '-', '*', '//'], repeat = len(array) - 1)
  )

  results = []
  for case in cases:
    result = reduce(
      lambda acc, val: calculate(acc, val, case), 
      enumerate(array[1:]), 
      array[0]
    )
    results.append(result)
  
  print(max(results))
  print(min(results))

N = int(input())
ARRAY = list(map(int, input().split()))
PLUS, MINUS, MULTIPLE, DIVIDE = list(map(int, input().split()))
solution(ARRAY, PLUS, MINUS, MULTIPLE, DIVIDE)