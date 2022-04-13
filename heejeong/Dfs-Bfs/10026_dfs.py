'''
적록색약
- 적록색약의 경우와 정상인의 경우
- R빨강 G초록 B파랑
- 같은 색상이 상하좌우로 인접한 경우-> 같은 구역에 속함.
- 방문여부를 담는 리스트를 따로 만들어줘야 함. 안 만들어주면 이전자리랑 현재자리랑 같은 색인지 비교 불가.
'''
import sys
sys.setrecursionlimit(10**6)
colors = ['R', 'G', 'B']
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, type):  # 정상인일 경우

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if type == 0:  # 정상인일 경우
            if data[nx][ny] != data[x][y]:
                continue
            # 방금 들어온 위치랑 4가지 방향위치랑 같은 색일 경우.
            if data[nx][ny] == data[x][y] and visited[nx][ny] == False:
                # 방문했으면 0으로 바꿔주기
                dfs(nx, ny, 0)  # 해당 위치에서 DFS 하기.
        else:  # 적록색약일 경우 - R, G랑 B 분리해서 같이 카운트해줘야 함.
            if data[x][y] == 'B':
                if data[nx][ny] == data[x][y] and visited[nx][ny] == False:
                    dfs(nx, ny, 1)
            else:
                if (data[nx][ny] == 'G' or data[nx][ny] == 'R') and visited[nx][ny] == False:
                    dfs(nx, ny, 1)


n = int(input())
data = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    data.append(list(input()))

cntNormal = 0  # 정상인일경우 개수 세기.
for i in range(n):
    for j in range(n):
        # 정상인일경우
        if data[i][j] in colors and visited[i][j] == False:
            #print("dfs 시작위치", data[i][j]) - 확인용
            dfs(i, j, 0)
            cntNormal += 1
visited = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if data[i][j] in colors and visited[i][j] == False:
            dfs(i, j, 1)
            cnt += 1

print(cntNormal, cnt)
