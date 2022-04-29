'''
포도주 시식 - 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램
- 경우의 수 잘 나눠주기 (생각하기)
- indexError해결 (리스트의 인덱스가 범위 밖인지 확인하기)
    : n이 1인 경우 for문으로 굳이 dp에 안 넣어줘도 되기 때문에
'''
n = int(input())  # 포도주 잔의 개수
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0] * (n+1)

if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = dp[1] + wine[2]

for i in range(3, n+1):  # 3~n
    dp[i] = max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])

print(dp[n])
