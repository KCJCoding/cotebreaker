'''
RGB거리
n개의 집. 빨 초 파 중 하나의 색. 집을 칠하는 비용의 최솟값
- 1번집의 색은 2번 집의 색과 같지 않아야 함.
- n번 집의 색은 n-1번 집의 색과 같지 않아야 함.
- i번의 집은 i-1, i+1번 집의 색과 같지 않아야 함.
**너무 dp에 강박해서 생각하다 안 풀렸음. dp 개념만 가져가기.
'''
n = int(input())  # 집의 수
cost = []
for _ in range(n):  # 빨 초 파 비용순서
    cost.append(list(map(int, input().split())))

for i in range(2, n+1):
    cost[i-1][0] = min(cost[i-2][1], cost[i-2][2]) + cost[i-1][0]
    cost[i-1][1] = min(cost[i-2][0], cost[i-2][2])+cost[i-1][1]
    cost[i-1][2] = min(cost[i-2][0], cost[i-2][1])+cost[i-1][2]

print(min(cost[n-1]))
