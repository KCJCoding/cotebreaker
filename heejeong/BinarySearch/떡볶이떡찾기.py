'''
적어도 M만큼은 떡을 가져가야 함.
'''

n, m = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
ddeok = list(map(int, input().split()))  # 떡의 개별 길이

start = 0
end = max(ddeok)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for item in ddeok:
        if item > mid:
            total += item - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
