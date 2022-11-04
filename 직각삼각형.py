def solution(edges):
    sorted_edges = sorted(edges)
    if sorted_edges[0] ** 2 + sorted_edges[1] ** 2 == sorted_edges[2] ** 2:
        return "right"
    else:
        return "wrong"


while True:
    edges = list(map(int, input().split()))
    if edges == [0, 0, 0]:
        break
    print(solution(edges))
