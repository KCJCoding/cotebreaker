# dp[k] = k원을 만드는 경우의 수
n, k = map(int, input().split())
dp = [0] * (k+1)
coins = []
for _ in range(n):
    coins.append(int(input()))

dp[0] = 1
for coin in coins:
    for i in range(1, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[k])

'''
x원을 이용해서 금액을 만들려면 그 금액이 x원보다 크거나 같아야 함.
1원만 사용하는 경우 dp[1]~dp[10]은 다 1
1원, 2원만 사용하는 경우 : 2원포함방법(dp[k-2])+2원포함X방법(dp[k])
x원 동전 추가할 때: x원포함방법 + x원포함X방법(dp[k])
'''



