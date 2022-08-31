from collections import deque

n = int(input()) 
start, target = map(int, input().split())
m = int(input())
visited = [0] * (n+1)

data = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split()) # 연결정보
    data[x].append(y)
    data[y].append(x)

q = deque()
q.append(start)

while q:
    now = q.popleft()
    # print(now)
    if now == target:
        break
    for node in data[now]:
        if not visited[node]:
            q.append(node)
            visited[node] = visited[now] + 1

if not visited[target]:
    print(-1)
else:
    print(visited[target])