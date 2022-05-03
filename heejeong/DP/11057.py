'''
오르막수
- 수의 자리가 오름차순을 이루는 수 (인접한 수가 같아도 오름차순)
- 수는 0으로 시작 가능
- 길이가 N인 오르막 수의 개수를 10007로 나눈 나머지 출력
- dp[i][j] : 길이가 i인 j로 끝나는 오르막 수의 개수 
'''
N = int(input())  # 수의 길이
dp = [[0] * 10 for _ in range(1001)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = 1
        else:
            dp[i][j] = dp[i][j-1]+dp[i-1][j]

print(sum(dp[N]) % 10007)
