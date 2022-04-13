'''
너비 우선 탐색
sys로 입력받아서 시간초과 해결
'''
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
cnt = 0
# print(visited)


def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)
