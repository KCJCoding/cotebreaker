'''
섬의 개수를 세는 프로그램
- 가로, 세로, 대각선으로 연결되어 있으면 갈 수 있음
- 1은 땅, 0은 바다
'''


def dfs(x, y):
    # 방문한 곳 0으로 바꿔줘야함.
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if data[nx][ny] == 1:
            data[nx][ny] = 0
            dfs(nx, ny)


w, h = map(int, input().split())  # 너비(가로) 높이(세로)
data = []
for _ in range(h):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

cnt = 0  # 섬의 개수를 저장하는 변수
for i in range(h):
    for j in range(w):
        if data[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)
