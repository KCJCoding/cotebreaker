# 현재위치(1,1) 미로의출구(N,M)
'''
괴물이 있는 부분은 0, 없는 부분은 1
탈출하기 위해 움직여야 하는 최소 칸의 개수
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산.
시작칸과 마지막칸은 항상 1.
=> bfs로 풀기.
'''
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # 공백없이 붙어서 입력됨.

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:  # 이동가능
                graph[nx][ny] = graph[x][y] + 1  # 누적해서 계산
                queue.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0, 0))  # (0, 0에서 시작하기 때문에 마지막 리턴 값은 n-1, m-1)
