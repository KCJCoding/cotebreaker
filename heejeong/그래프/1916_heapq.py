'''
heapq모듈을 통새허 원소를 추가하거나 삭제한 리스트가 그냥 최소힙
'''
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)  # 방문노드 체크
distance = [INF] * (N+1)  # 최단거리 기록

for _ in range(M):
    start, finish, cost = map(int, input().split())
    graph[start].append((finish, cost))
start_city, finish_city = map(int, input().split())  # 시작도시, 도착도시


def dijkstra(start_city):
    distance[start_city] = 0
    heap = []  # 최소힙 생성
    heapq.heappush(heap, (0, start_city))
    while heap:
        cost, now_city = heapq.heappop(heap)
        if distance[now_city] < cost:  # 다이렉트 거리가 최소인 경우는 유지
            continue
        for node in graph[now_city]:  # 해당 노드에 연결된 다른 노드들
            next_cost = cost + node[1]  # 다음 노드까지의 비용
            if distance[node[0]] > next_cost:
                distance[node[0]] = next_cost  # 최소비용 업데이트
                heapq.heappush(heap, (next_cost, node[0]))


dijkstra(start_city)
print(distance[finish_city])
