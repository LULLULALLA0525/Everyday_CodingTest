INF = 10000000

def solution(maze, rowOfJ, colOfJ, rowOfF, colOfF):
    result = 0
    return result

def mazeValue(s):
    if s is "#":
        return INF
    elif s is "J":
        rowOfJ

r, c = list(map(int, input().split()))
maze = [[] for _ in range(r)]
for row in range(r):
    maze[row] = list(map(int, input().split()))