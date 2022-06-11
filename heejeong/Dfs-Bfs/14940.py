'''
목표지점까지의 거리 구하기 - 가로와 세로로만 움직이기 가능
0: 갈 수 없는 땅
1: 갈 수 있는 땅
2: 목표지점
-> 각 지점에서 목표 지점까지의 거리 출력. 
- 목표지점을 기준으로 각 위치까지의 거리를 저장하고 출력
-> 목표지점 위치를 알아내는 함수를 따로 만들어줬더니 통과됨.
'''
from collections import deque
import sys
input = sys.stdin.readline


def find_start():
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                return i, j


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())  # 세로, 가로
data = []
dest_i, dest_j = 0, 0  # 목표지점 위치 넣어주기
cnt = 0
for i in range(N):
    data.append(list(map(int, input().split())))
dest_i, dest_j = find_start()

visited = [[-1] * M for _ in range(N)]
q = deque()
q.append((dest_i, dest_j))
visited[dest_i][dest_j] = 0  # 방문처리

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
            if data[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            elif data[nx][ny] == 0:
                visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
