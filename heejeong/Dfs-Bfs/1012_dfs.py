t = int(input()) #테스트케이스 수
for _ in range(t):
    m, n, k = map(int, input().split()) #m: 가로길이(열) n: 세로길이(행)
    graph = [[0] * m for _ in range(n)] #배추 위치 정보를 담을 리스트

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = -1
            dfs(x-1, y) #상
            dfs(x+1, y) #하
            dfs(x, y-1) #좌
            dfs(x, y+1) #우
            return True
        return False

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)

