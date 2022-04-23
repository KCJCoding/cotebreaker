'''
파도반 수열
규칙 : dp[i] = dp[i-2]+dp[i-3]

'''
dp = [0, 1, 1, 2]
t = int(input())  # 테스트케이스 개수
for _ in range(t):

    n = int(input())

    for i in range(3, n+1):
        dp.append(dp[i-2]+dp[i-3])
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])
