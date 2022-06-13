'''
가로-세로 : 반대로 생각하기
max를 만나는 기점으로 나누기.
max를 만나기 전까지의 max값.
특정위치에 물이 고이기 위해서는 자신보다 더 높은 블록으로 오른쪽과 왼쪽으로 둘러싸여 있어야 함.
첫번째 칸과 마지막 칸은 물이 고일 수ㅜ 없음.
'''
H, W = map(int, input().split())  # 세로, 가로 -> 가로, 세로 로 생각하기
data = [[0] * H for _ in range(W)]
nums = list(map(int, input().split()))
max_num = max(nums)
cntMax = 0
result = 0
for i in range(1, len(nums)-1):
    maxLeft = max(nums[:i])
    maxRight = max(nums[i+1:])
    mid = min(maxLeft, maxRight)
    if mid > nums[i]:
        result += mid - nums[i]

print(result)
