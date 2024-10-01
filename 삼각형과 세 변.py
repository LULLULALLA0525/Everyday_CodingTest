import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(edges):
  if max(edges) * 2 >= sum(edges):
    return "Invalid"

  if edges[0] == edges[1] and edges[1] == edges[2]:
    return "Equilateral"
  
  if edges[0] == edges[1] or edges[1] == edges[2] or edges[2] == edges[0]:
    return "Isosceles"

  return "Scalene"

ANSWERS = []
while True:
  EDGES = list(map(int, input().split()))
  if EDGES == [0, 0, 0]:
    break

  ANSWERS.append(solution(EDGES))

for ANSWER in ANSWERS:
  print(ANSWER)