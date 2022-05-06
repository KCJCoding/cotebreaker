'''
쉬운 계단 수
- 인접한 모든 자리의 차이가 1 : 계단수
-길이가 N인 계단 수가 총 몇개인지
-0으로 시작하면 계단수가 아님.
- 끝자리가 0,9인 경우와 끝자리가 1~8인 경우 나누어주기.
- 인덱스에러 : 리스트 잘 보기
'''
n = int(input())
dp = [[0]*10 for _ in range(101)]  # dp[i][j] : 길이가 n인 끝의자리 숫자가 j인 개수가 저장됨.
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)