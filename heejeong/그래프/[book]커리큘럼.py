'''
SSAFY 코테 2번 문제와 비슷한 유형.
특정 강의가 주어졌을 때, 해당 강의를 듣기 위해 걸리는 시간
- 위상정렬 사용
- indegree : 특정한 노드로 '들어오는' 간선의 개수
- data = 강의시간, 그 강의를 듣기 위해 들어야 하는 선수과목
'''
from collections import deque
import copy

N = int(input())  # 강의의 수
indegree = [0] * (N+1)
time = [0] * (N+1)  # 각 과목의 강의시간
graph = [[] for _ in range(N+1)]  # 해당 인덱스가 선수과목인 과목들이 들어있음

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 강의 시간 초기화
    for x in data[1:-1]:  # 선수과목들
        indegree[i] += 1
        graph[x].append(i)

# 위상정렬 함수


def topologySort():
    result = copy.deepcopy(time)  # 결과를 담을 리스트
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:  # 선수과목이 없는 경우
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:  # now를 들은 후 들을 수 있는 과목들
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N+1):
        print(result[i])


topologySort()
