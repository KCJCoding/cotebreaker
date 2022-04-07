# DFS로 해결한 문제
computer = int(input())
pair = int(input())

graph = [[0] * (computer+1) for _ in range(computer+1)]
visit = [0 for _ in range(computer+1)]

for i in range(pair):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    visit[v] = 1
    for i in range(1, computer+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


dfs(1)

count = 0
for i in range(2, computer+1):
    if visit[i] == 1:
        count += 1

print(count)
