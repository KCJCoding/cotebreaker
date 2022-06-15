'''
최소비용구하기
'''
import heapq

INF = int(1e9)
N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)  # 방문노드 체크
distance = [INF] * (N+1)  # 최단거리 기록


def get_smallest_node():
    # 방문하지 않은 노드 중에서 비용이 최소인 노드의 index 리턴
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start_city):
    distance[start_city] = 0
    visited[start_city] = True
    for node in graph[start_city]:  # 시작노드에 인접한 노드들에 대한 거리 계산
        distance[node[0]] = node[1]

    for _ in range(N-1):  # 시작노드 제외한 나머지 다른 노드들처리
        now = get_smallest_node()
        visited[now] = True  # 방문처리
        for next in graph[now]:  # 해당 노드와 연결된 다른 노드
            cost = distance[now] + next[1]  # now까지의 비용+다음에 갈 노드까지의 비용
            if cost < distance[next[0]]:  # now까지의 다이렉트 비용 보다 작은 경우
                distance[next[0]] = cost


for _ in range(M):
    start, finish, cost = map(int, input().split())
    graph[start].append((finish, cost))

start_city, finish_city = map(int, input().split())  # 시작도시, 도착도시

dijkstra(start_city)

print(distance[finish_city])
