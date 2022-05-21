'''
나무자르기
- 적어도 M미터 가져가려고 함
- 절단기에 설정할 수 있는 높이의 최댓값 구하기
- [이코테]떡볶이떡찾기 문제와 비슷
'''
import sys  # '시간초과'
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2

    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total >= M:  # 절단기 높이 높이기
        result = mid  # 절단기 높이의 최댓값이 정답
        start = mid + 1
    else:  # total < M -> 절단기 높이 낮추기
        end = mid - 1
print(result)
