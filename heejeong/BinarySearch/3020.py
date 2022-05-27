'''
개똥벌레
- 파괴해야 하는 장애물의 최솟값과 구간의 수를 출력
- 종유석과 석순 구분짓기 top, bottom
- 종유석 : 높이가 작아질수록 지나가는 조유석 증가
- 석순은 높이가 높아질수록 통과하는 개수가 증가
- 종유석과 석순 각각 구분. 각각의 길이에 대한 누적합 계산
- 높이 H부터 높이 1까지의 누적합 계산 : 높이i의 배열값은 높이 i이상의 모든 석순 개수.
'''
import sys
input = sys.stdin.readline  # 시간초과 해결
N, H = map(int, input().split())
top = [0] * (H+1)  # 종유석
bottom = [0] * (H+1)  # 석순

min_count = N  # 파괴해야 하는 장애물의 최솟값
range_count = 0  # 최솟값이 나타나는 구간의 수

for i in range(N):
    if i % 2 == 0:  # 석순
        bottom[int(input())] += 1
    else:  # 종유석
        top[int(input())] += 1

# 누적합 계산
for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]

for i in range(1, H+1):
    if min_count > (bottom[i] + top[H-i+1]):
        min_count = bottom[i] + top[H-i+1]
        range_count = 1
    elif min_count == (bottom[i] + top[H-i+1]):
        range_count += 1

print(min_count, range_count)
