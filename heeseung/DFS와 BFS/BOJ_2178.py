# 최단거리를 구해야 할 경우 DFS보다 BFS가 더 적합하다. DFS는 처음으로 발견되는 해답이 최단거리라는 것이 보장되지 않는다. 반면 BFS는 현재 노드에서 가까운 곳부터 찾기 때문에 경로 탐색 시 첫번째로 찾아지는 해답이 곧 최단거리이다.

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))
