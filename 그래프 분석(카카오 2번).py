import sys
limit_number = 1000000
sys.setrecursionlimit(limit_number)

def traverse(graph, starting_node, node, isStart):
    if not isStart and node == starting_node:
        return 1    # 도넛
    elif node not in graph:
        return 2    # 막대
    elif len(graph[node]) == 2:
        return 3    # 8자
    else:
        return traverse(graph, starting_node, graph[node][0], False)

def solution(edges):
    answer = [0, 0, 0, 0]

    graph = {}
    reversed_graph = {}     # 간선의 방향이 바뀐 그래프, 생성된 정점을 찾기 위함
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

        if edge[1] in reversed_graph:
            reversed_graph[edge[1]].append(edge[0])
        else:
            reversed_graph[edge[1]] = [edge[0]]
    
    for node in graph:
        if len(graph[node]) >= 2 and node not in reversed_graph:
            # 2개 이상의 정점으로 나가며, 들어오는 정점은 없는 경우
            answer[0] = node
            break
    
    starting_nodes = graph[answer[0]]
    for node in starting_nodes:
        graph_type = traverse(graph, node, node, True)
        answer[graph_type] += 1

    return answer
