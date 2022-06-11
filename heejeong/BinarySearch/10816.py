from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
numsDic = Counter(nums)
# numsDic = {}
# for num in numsDic:
#     if num not in numsDic:
#         numsDic[num] = 1
#     else:
#         numsDic[num] += 1

m = int(input())
check_nums = list(map(int, input().split()))

for target in check_nums:
    start = 0
    end = n-1
    while(start <= end):
        mid = (start+end) // 2
        if nums[mid] == target:
            break
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if nums[mid] == target:
        print(numsDic[target], end=' ')
    else:
        print(0, end=' ')
