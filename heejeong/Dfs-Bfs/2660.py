from collections import deque
# 회장은 회원들 중에서 점수가 가장 작은 사람. 회장의 점수와 회장이 될 수 있는 사람의 수 출력
def bfs(idx):
    visited = [-1] * (n+1)
    visited[idx] = 0 #방문 표시
    q = deque([idx])
    while q:
        v = q.popleft()
        for node in graph[v]: # 각 노드까지의 거리 구해서 최댓값 반환
            if visited[node] == -1:
                visited[node] = visited[v] + 1
                q.append(node)
    return max(visited)

n = int(input()) # 회원의 수
graph = [[] for _ in range(n+1)]
score = [0] * (n+1)
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n+1):
    score[i] = bfs(i)

for i in range(1, n+1):
    if min(score[1:]) == score[i]:
        result.append(i)
print(min(score[1:]), len(result))
for k in result:
    print(k, end=' ')
# print(*result)