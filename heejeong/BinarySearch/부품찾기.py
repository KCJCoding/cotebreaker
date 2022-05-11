def binarySearch(nums, target, start, end):

    while start <= end:
        mid = (start+end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    return None  # 부품에 없는 경우


n = int(input())  # 부품 종류개수
nums = list(map(int, input().split()))
m = int(input())  # 손님이 요청한 부품
order = list(map(int, input().split()))

nums.sort()

for i in order:
    result = binarySearch(nums, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
