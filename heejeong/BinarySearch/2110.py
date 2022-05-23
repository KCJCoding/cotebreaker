'''
공유기 설치
- 가장 인접한 두 공유기 사이의 거리를 최대한 크게
- 집 위치에 공유기 설치
ex) 1 2 4 8 9 ->1, 4, 8 or 1, 4, 9
'''
import sys
input = sys.stdin.readline  # 시간초과 때문에 추가
N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
result = 0
start, end = 1, house[-1]-house[0]  # 최소거리, 최대거리
# 중간값을 기준으로 집의 개수를 셌을 때,
# C보다 크면, 최솟값을 mid+1
# C보다 작으면, 최댓값을 mid-1
# 최솟값과 최댓값이 같아질 때까지 반복
while start <= end:
    mid = (start+end) // 2
    old = house[0]
    cnt = 1  # 거리를 mid로 두었을 때 가능한 집의 개수를 세는 변수
    for i in range(1, len(house)):
        if house[i] >= old+mid:
            cnt += 1
            old = house[i]
    if cnt >= C:
        start = mid + 1
        result = mid  # 최댓값
    else:
        end = mid - 1

print(result)
