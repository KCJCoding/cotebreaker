from collections import deque

m, n = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([])
res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])


bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max())
print(res - 1)
