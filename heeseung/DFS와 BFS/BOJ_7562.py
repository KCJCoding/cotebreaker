from collections import deque

case = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(nx, ny, mx, my):
    q = deque()
    q.append([nx, ny])
    graph[nx][ny] = 1
    while q:
        a, b = q.popleft()
        if a == mx and b == my:
            print(graph[mx][my] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and graph[x][y] == 0:
                q.append([x, y])
                graph[x][y] = graph[a][b] + 1


for i in range(case):
    n = int(input())
    now_x, now_y = map(int, input().split())
    move_x, move_y = map(int, input().split())

    graph = [[0] * n for _ in range(n)]
    bfs(now_x, now_y, move_x, move_y)
