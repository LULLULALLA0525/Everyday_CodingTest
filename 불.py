from collections import deque

INF = -1
X = 0
Y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(j_maze, position_of_j, f_maze, position_of_f):
    f_queue = deque()
    f_queue.append(position_of_f)
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(f_maze[y]) or ny < 0 or ny >= len(f_maze):  # out of range
                continue
            elif f_maze[ny][nx] == 0:  # 아직 가보지 않은 곳
                f_maze[ny][nx] = f_maze[y][x] + 1
                f_queue.append([nx, ny])
            elif f_maze[ny][nx] == INF or f_maze[ny][nx] <= f_maze[y][x]:  # 벽 혹은 이미 빠른 경로가 있는 곳
                continue
            else:   # 이미 지나간 경로지만 더 빠른 경로를 찾은 경우
                f_maze[ny][nx] = f_maze[y][x] + 1
                f_queue.append([nx, ny])

    j_queue = deque()
    j_queue.append(position_of_j)
    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(j_maze[y]) or ny < 0 or ny >= len(j_maze):  # out of range
                continue
            elif f_maze[ny][nx] <= j_maze[y][x]:    # 불길이 먼저 도착한 곳
                continue
            elif j_maze[ny][nx] == 0:  # 아직 가보지 않은 곳
                j_maze[ny][nx] = j_maze[y][x] + 1
                j_queue.append([nx, ny])
            elif j_maze[ny][nx] == INF or j_maze[ny][nx] <= j_maze[y][x]:  # 벽 혹은 이미 빠른 경로가 있는 곳
                continue
            else:  # 이미 지나간 경로지만 더 빠른 경로를 찾은 경우
                j_maze[ny][nx] = j_maze[y][x] + 1
                j_queue.append([nx, ny])


def solution(maze):
    position_of_j = [0, 0]
    position_of_f = [0, 0]
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == "J":
                position_of_j = [column, row]
            elif maze[row][column] == "F":
                position_of_f = [column, row]

    j_maze = []
    f_maze = []
    for cells in maze:
        j_cells = []
        f_cells = []
        for cell in cells:
            if cell == "#":
                j_cells.append(INF)
                f_cells.append(INF)
            else:
                j_cells.append(0)
                f_cells.append(0)
        j_maze.append(j_cells)
        f_maze.append(f_cells)

    print(j_maze)
    print(f_maze)

    bfs(j_maze, position_of_j, f_maze, position_of_f)

    print(j_maze)
    print(f_maze)


r, c = list(map(int, input().split()))
m = []
for _ in range(r):
    m.append(list(input().split()))

print(solution(m))
