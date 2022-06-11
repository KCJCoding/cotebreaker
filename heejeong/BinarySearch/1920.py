'''
수찾기 - 이코테 부품찾기 문제와 비슷
'''


def binarySearch(arr, target, left, right):
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
check_nums = list(map(int, input().split()))

for i in check_nums:
    result = binarySearch(nums, i, 0, n-1)
    if result != None:
        print(1)
    else:
        print(0)
