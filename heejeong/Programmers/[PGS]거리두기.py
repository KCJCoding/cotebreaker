'''
앉아있는 자리P가 출발지점
'''
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(data):
    P_start = []  # P의 좌표

    for i in range(5):
        for j in range(5):
            if data[i][j] == 'P':
                P_start.append([i, j])

    for start in P_start:
        queue = deque([start])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]

        visited[start[0]][start[1]] = 1  # P의 위치는 방문 완료

        while queue:
            x, y = queue.popleft()

            for i in range(4):  # 상하좌우 확인 ->
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if data[nx][ny] == 'X':
                        continue
                    elif data[nx][ny] == 'O':
                        queue.append([nx, ny])
                        distance[nx][ny] = distance[x][y] + 1
                    elif data[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        if bfs(i) is None:
            answer.append(1)
        else:
            answer.append(bfs(i))

    return answer
