import sys

input = lambda: sys.stdin.readline()

def solution(string):
  found = 0
  for char in string:
    if char == "KOREA"[found % 5]:
      found += 1
  
  return found

STRING = input().strip()
print(solution(STRING))