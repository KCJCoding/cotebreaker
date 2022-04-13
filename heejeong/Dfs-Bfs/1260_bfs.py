from collections import deque


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:  # 이어져있는 노드 중 방문하지 않은 노드만 방뮨
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, v = map(int, input().split())  # 정점, 간선, 탐색시작정점
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]  # 방문 처리노드

# dfs수행결과
bfs(graph, v, visited)
# bfs수행결과
