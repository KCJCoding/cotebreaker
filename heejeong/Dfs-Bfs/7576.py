'''인접노드만 방문하기 때문에 bfs로 풀기'''
from collections import deque

m, n = map(int, input().split())  # 가로 세로
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

queue = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])  # 익은토마토 위치 넣어주기


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                # 안익은토마토 익혀주기
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)  # 다 익히지 못했기 때문에 -1 출력
            exit(0)
    result = max(result, max(i))
print(result - 1)
