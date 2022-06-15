'''
백준 1647번과 동일
- 길의 유지비의 합을 최소로 할 때
- 크루스칼 알고리즘으로 최소 신장트리를 찾은 뒤, 가장 비용이 큰 간선 지우기
'''
import sys
input = sys.stdin.readline  # 시간초과로 추가해줌


def find_parent(parent, node):  # 사이클 방지를 위함.
    # 부모노드 찾기
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, x, y):  # 신장트리에 포함되면 루트노드 변경해줘야 함
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 수가 더 작은 루트노드에 포함시켜주기(루트노드 변경)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())  # 집의 개수, 길의 개수
parent = [0] * (N+1)

edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()  # 유지비용순으로 오름차순
last = 0

# 유지비가 작은 순으로 연결시켜주면서 최소신장트리 만들기
# 맨 마지막에 유지비가 가장 큰 간선 제거 -> 2개로 분리
for edge in edges:
    cost, a, b = edge  # 하나씩 꺼내기
    if find_parent(parent, a) != find_parent(parent, b):  # 루트노드가 다르면
        union_parent(parent, a, b)  # 신장트리에 추가해주기
        result += cost  # 총 비용
        last = cost  # 맨 마지막이 가장 비용이 큰 유지비가 들어오게 됨
print(result - last)
