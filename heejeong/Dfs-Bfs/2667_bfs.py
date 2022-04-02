from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(data, a, b):
    n = len(data)
    queue = deque()
    queue.append((a, b))
    data[a][b] = 0  # 방문한 자리 0으로 바꿔주기
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt  # 아파트 수 리턴


n = int(input())  # 지도크기
data = []
for _ in range(n):
    data.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            cnt.append(bfs(data, i, j))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
