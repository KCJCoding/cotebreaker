'''
6가지 방향 - 위, 아래, 오른쪽, 왼쪽, 앞, 뒤
1: 익은 토마토
0: 익지 않은 토마토
-1 : 토마토 X
bfs로 풀기

'''
from collections import deque

M, N, H = map(int, input().split())
ans = 0
tomato = []
for _ in range(H):
    tomato.append([list(map(int, input().split())) for _ in range(N)])

# print(tomato) #확인용

dz = [0, 0, 0, 0, -1, 1] # 3차원 - 앞 뒤 좌 우 상 하
dx = [-1, 1, 0, 0, 0, 0] # 세로 - 앞 뒤 좌 우 상 하
dy = [0, 0, -1, 1, 0, 0] # 가로 - 앞 뒤 좌 우 상 하

q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 1:
                q.append((h, i, j)) # 토마토 위치 넣어주기

cnt_ripen = len(q) # 초기 익은 토마토 개수
cnt_not_ripen = (H*M*N) - cnt_ripen # 초기 익지 않은 토마토

while q:
    height, x, y = q.popleft()
    for i in range(6):
        nheight, nx, ny = height + dz[i], x + dx[i], y + dy[i] 
        if 0 <= nheight < H and 0 <= nx < N and 0 <= ny < M:
            if tomato[nheight][nx][ny] == 0: 
                tomato[nheight][nx][ny] = tomato[height][x][y] + 1
                q.append((nheight, nx, ny))
    # print("토마토 변화", tomato) # 확인용

max_days = 0
cnt_zero = 0
for k in range(H):
    for i in range(N):
        max_days = max(max(tomato[k][i]), max_days)
        cnt_zero += tomato[k][i].count(0)

if cnt_not_ripen == 0: # 처음부터 다 익어있는 상황
    print(0)
elif cnt_zero != 0: # 모두 익지 못하는 상황
    print(-1)
else:
    print(max_days-1)


