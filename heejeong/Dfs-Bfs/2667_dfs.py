# dfs - 속하는 집 이어져있는 곳 파고들기.
n = int(input())  # 지도크기
data = []
for _ in range(n):
    data.append(list(map(int, input())))
cnt_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if data[x][y] == 1:
        global cnt
        cnt += 1
        data[x][y] = 0  # 방문했으니까 0으로 바꿔주기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


cnt = 0  # 아파트 수
result = 0  # 단지 수

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt_list.append(cnt)  # 아파트 수 넣어주기 - dfs의 cnt
            result += 1  # 단지 수
            cnt = 0


cnt_list.sort()
print(result)
for i in range(len(cnt_list)):
    print(cnt_list[i])
