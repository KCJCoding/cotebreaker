'''
구멍 뚫려 있는 부분 : 0
칸막이가 존재하는 부분 : 1
각각 이동하면서 상하좌우 확인 -> 방문처리
만들 수 있는 아이스크림의 개수 출력
'''

n, m = map(int, input().split())  # 세로, 가로
data = []
for _ in range(n):
    data.append(list(map(int, input())))

cnt = 0  # 아이스크림 개수를 저장하는 변수

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동 불가
        if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny] == 1:
            continue
        if data[nx][ny] == 0:  # 이동 가능
            data[nx][ny] = 1  # 바꿔주기
            dfs(nx, ny)
            return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:  # 0인 위치에서 dfs수행
            cnt += 1
print(cnt)
