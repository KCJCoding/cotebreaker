'''
가장 긴 증가하는 부분 수열 - 가장 긴 증가하는 수열의 길이 출력
dp : 자신을 포함하여 만들 수 있는 부분수열 크기 저장
'''
N = int(input())  # 수열의 크기
data = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):  # 자기 자신보다 앞에 있는 요소 모두 확인
        if data[j] < data[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
