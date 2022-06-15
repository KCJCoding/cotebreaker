'''
처음에는 모든 학생이 서로 다른 팀.
0 : 팀 합치기
1: 같은 팀 여부 확인
'''


def find_parent(data, node):
    if data[node] != node:  # 부모노드가 자기자신에서 달라진 경우
        data[node] = find_parent(data, data[node])  # data[node]의 부모노드 찾ㄱ지
    return data[node]


def unionTeam(data, x, y):
    x = find_parent(data, x)  # 부모 노드가 다른 경우 합쳐주기
    y = find_parent(data, y)

    if x < y:
        data[y] = x
    else:
        data[x] = y


N, M = map(int, input().split())
graph = [0]*(N+1)
for i in range(N+1):  # 초기 : 모두 서로 다른 팀
    graph[i] = i

for _ in range(M):
    x, a, b = map(int, input().split())
    if x == 0:
        # 팀 합치기 연산
        unionTeam(graph, a, b)
    if x == 1:
        # 같은 팀 여부 확인 연산
        if find_parent(graph, a) != find_parent(graph, b):
            print('NO')
        else:
            print('YES')
