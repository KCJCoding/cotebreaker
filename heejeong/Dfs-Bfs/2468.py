'''
물에 잠기지 않는 영역의 최대 개수 계산
- bfs너비우선탐색, 안전한 영역인 경우 큐에 넣기. bfs끝날때마다 +1 로 안전영역 계산
- 흰색 영역 찾아서 큐에 넣어주기. n보다 큰 경우
- 최댓값 갱신해주기
'''
from collections import deque

def bfs(a, b, nheight):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if data[nx][ny] > nheight and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
N = int(input()) #행과 열의 개수
data = []
maxNum = 0
maxZone = 0
for i in range(N):
    data.append(list(map(int, input().split())))
    maxNum = max(max(data[i]), maxNum)

for nHeight in range(1, maxNum): # 비교할 높이
    visited = [[0] * N for _ in range(N)]
    safeZone = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > nHeight and visited[i][j] == 0: # 해당 높이보다 높은 경우, 안전->bfs 수행
                bfs(i, j, nHeight)
                safeZone += 1
    if safeZone > maxZone: #안전영역의 최댓값 갱신해주기.
        maxZone = safeZone

print(maxZone)