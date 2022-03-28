'''
1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력
'''
n = int(input()) #컴퓨터의 수
m = int(input()) #연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1

visited = [False] * (n+1) #해당 컴퓨터 확인했는지여부

dfs(graph, 1, visited)

print(cnt)

