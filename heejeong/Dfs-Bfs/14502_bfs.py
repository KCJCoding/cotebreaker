'''
연구소 - 바이러스를 막기 위해 벽을 세우려고 함.
안전영역 크기의 최댓값 구하기.
0:빈칸
1:벽
2:바이러스가 존재
바이러스는 상하좌우 인접한 빈칸으로 모두 퍼질 수 있음. 벽 3개 세우기.
빈칸에만 벽 세우기 가능.
인접노드만 방문. bfs
'''
from collections import deque
import copy


def bfs(x, y):
    queue = deque()
    tmp_data = copy.deepcopy(data)
    for i in range(n):
        for j in range(m):
            if tmp_data[i][j] == 2:  # 바이러스가 있을 때, 큐에 넣기
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_data[nx][ny] == 0:  # 비어있을 때, 바이러스 퍼지기 가능
                tmp_data[nx][ny] = 2
                queue.append((nx, ny))  # 바이러스 퍼진 위치 큐에 넣기.

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_data[i].count(0)  # 0개수 세기
    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:  # 벽을 3개 다 세운 경우, 바이러스 퍼트리기
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:  # 벽 세우기 가능
                data[i][j] = 1
                makeWall(cnt+1)  # 벽 또 세우기
                data[i][j] = 0  # bfs 수행 후 , 벽 지우기
                '''
                백트래킹 - (다른 세 위치를 골라야하기 때문에)
                다시 벽을 세우고 BFS를 수행하고 벽을 지우는 방식을 반복
                '''


n, m = map(int, input().split())  # n 세로, m 가로
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
makeWall(0)
print(answer)
