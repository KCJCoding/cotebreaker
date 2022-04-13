# dfs : 깊이 우선 탐색 - 최대한 파고들어서 탐색.

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


n, m, v = map(int, input().split())  # 정점, 간선, 탐색시작정점
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
dfs(v)
