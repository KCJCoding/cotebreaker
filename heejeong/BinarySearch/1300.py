'''
임의의 숫자 M을 골라서 K번째 숫자인지 판단해보는 문제
내가 구하고자 하는 K번째 인덱스까지만 알면 된다.
'''
N = int(input())
K = int(input())

start, end = 1, K
answer = 0

while start <= end:
    mid = (start+end) // 2
    tmp = 0
    for i in range(1, N+1):
        tmp += min(mid//i, N)
    if tmp >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)