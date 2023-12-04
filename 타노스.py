import sys

input = lambda: sys.stdin.readline()

def solution(s):
  counts = [s.count(i) for i in range(2)]
  
  new_s = []
  new_counts = [0, 0]
  for c in s:
    new_counts[c] += 1
    if c == 0:
      if new_counts[0] <= counts[0] // 2:
        new_s.append("0")
    else:
      if new_counts[1] > counts[1] // 2:
        new_s.append("1")

  return "".join(new_s)

S = list(map(int, list(input().strip())))
print(solution(S))