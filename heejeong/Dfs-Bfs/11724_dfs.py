'''
깊이 우선 탐색
방향없는 그래프 -> 연결 요소의 개수 구하기 (연결묶음 개수 구하기.)

1번부터 탐색하면서 해당 노드의 연결된 노드들
방문여부가 false일 때만 방문.

방문이 끝나면 cnt += 1
'''
# 추가부분 - (+dfs함수 내에 return 문 다 삭제) recursion error 해결
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
#
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
visited = [False] * (n+1)  # 방문여부
cnt = 0  # 연결 요소 개수를 저장하는 변수


def dfs(node):
    visited[node] = True
    for j in graph[node]:
        if visited[j] == False:
            visited[j] = True
            dfs(j)  # 다시 연결된 것 탐색.


for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)
