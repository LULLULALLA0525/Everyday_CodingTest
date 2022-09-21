INF = int(1e9)

def get_nearest_node(N, distance, visited):
	dist = INF
	index = 0
	for node_idx in range(1, N + 1):
		if not visited[node_idx]:
			if distance[node_idx] < dist:
				dist = distance[node_idx]
				index = node_idx
	return index

def solution(N, road, K):
	graph = [{} for _ in range(N + 1)]
	for r in road:
		src, dest, dist = list(r)
		if dest in graph[src].keys():
			if dist < graph[src][dest]:
				graph[src][dest] = dist
				graph[dest][src] = dist
		else:
			graph[src][dest] = dist
			graph[dest][src] = dist
	
	distance = [INF] * (N + 1)					# 0을 제외한 노드의 개수를 처리하기 위함
	visited = [False] * (N + 1)

	distance[1] = 0
	visited[1] = True
	for near in graph[1].keys():
		distance[near] = graph[1][near]

	for _ in range(N - 1):
		node = get_nearest_node(N, distance, visited)
		visited[node] = True
		for near in graph[node].keys():
			dist = distance[node] + graph[node][near]
			if dist < distance[near]:
				distance[near] = dist

	answer = 0
	for d in distance:
		if d <= K:
			answer += 1
	
	return answer


N = int(input())									# 총 노드의 개수
# 5
temp = list(input().split(","))
road = [list(map(int, t.split())) for t in temp]	# 연결된 간선의 정보를 담은 리스트(src, dest, distance)
# 1 2 1,2 3 3,5 2 2,1 4 2,5 3 1,5 4 2
K = int(input())									# 허용 가능한 최소 배달 시간
# 3

print(solution(N, road, K))