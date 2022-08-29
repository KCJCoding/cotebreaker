'''
트리처럼 생각, 루트와 노드
'''
n = int(input()) 
start, target = map(int, input().split())
m = int(input())

data = [[] for _ in range(n+1)]
visited = [0] * (n+1)
ans = 0

for _ in range(m):
    x, y = map(int, input().split()) # 연결정보
    data[x].append(y)
    data[y].append(x)

def dfs(now):
    if now == target:
        return
    
    for node in data[now]:
        if not visited[node]:
            visited[node] = visited[now] + 1
            dfs(node)

dfs(start)

if not visited[target]:
    print(-1)
else:
    print(visited[target])