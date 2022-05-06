'''
영역 구하기
- 몇개로 분리되고, 분리된 공간 오름차순으로 정렬해서 리턴
'''
from collections import deque


def bfs(m, n):
    queue = deque()
    queue.append((m, n))
    data[m][n] = 1
    sum = 0
    while queue:
        x, y = queue.popleft()
        sum += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if data[nx][ny] == 0:
                queue.append((nx, ny))
                data[nx][ny] = 1  # 방문했기 때문에 값을 1로 바꿔주기.
    #     print("빈부분 합", sum)
    # print(data)
    # print("최종 sum", sum)
    return sum


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N, K = map(int, input().split())
data = [[0] * N for _ in range(M)]
for _ in range(K):
    x, y, xx, yy = map(int, input().split())
    for i in range(y, yy):
        for j in range(x, xx):
            data[i][j] = 1

result = []  # 비어있는 부분 넓이 저장해줄 변수
size = 0
for i in range(M):
    for j in range(N):
        if data[i][j] == 0:
            size = bfs(i, j)
            # print(i, j)
            result.append(size)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i], end=" ")
