from collections import deque
# 이동횟수 출력!!!

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

t = int(input())  # 테스트케이스의 개수
for _ in range(t):
    n = int(input())  # 체스판의 길이
    current_x, current_y = map(int, input().split())  # 현재있는칸
    target_x, target_y = map(int, input().split())  # 이동하려는 칸

    # visited = [[False] * n for _ in range(n)] #체스판의 방문여부
    visited = [[0] * n for i in range(n)]

    queue = deque()
    queue.append((current_x, current_y))
    visited[current_x][current_y] = 0

    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:  # 현재위치랑이동하려는 칸이 같므면 종료
            break
        # 8가지 방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1  # 누적해서 더해주기
                queue.append((nx, ny))  # 큐에 넣어주기

    print(visited[target_x][target_y])
