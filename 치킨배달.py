import sys
from itertools import combinations

input = lambda: sys.stdin.readline()

def printInfo(houses):
  for house in houses:
    print(str(house[0]) + "에 있는 집은 치킨거리가 " + str(min(map(lambda x: x[1], house[1]))) + "입니다.")
    for chicken in house[1]:
      print("\t" + str(chicken[0]) + "에 있는 치킨집과 " + str(chicken[1]) + "만큼 떨어져 있습니다.")

def chicken_distance_of_city(houses):
  return sum(map(lambda house: min(map(lambda chicken: chicken[1], house[1])), houses))

def chicken_distance_of_city_with(houses, remained_chickens_points):
  result = 0
  for house in houses:
    remained_chickens = filter(lambda chicken: chicken[0] in remained_chickens_points, house[1])
    chicken_distance = min(map(lambda chicken: chicken[1], remained_chickens))
    result += chicken_distance
  return result

def solution(m, city):
  chickens = []   #치킨집의 좌표
  for y in range(len(city)):
    for x in range(len(city)):
      if city[y][x] == 2:
        chickens.append([x, y])

  houses = []   #집의 좌표, 이후 치킨집 각각에 대한 (치킨집 좌표, 치킨 거리)를 원소로 갖는 리스트
  for y in range(len(city)):
    for x in range(len(city)):
      if city[y][x] == 1:
        chicken_distances = [(chicken, abs(x - chicken[0]) + abs(y - chicken[1])) for chicken in chickens]
        houses.append([(x, y), chicken_distances])

  cases = combinations(chickens, m)
  result = min(map(lambda x: chicken_distance_of_city_with(houses, x), cases))
  return result

N, M = list(map(int, input().split()))
CITY = []
for _ in range(N):
  CITY.append(list(map(int, input().split())))

print(solution(M, CITY))