'''
개미전사
'''
n = int(input())  # 식량창고의 수
food = list(map(int, input().split()))

result = 0  # 결과를 저장하는 변수
dp = [0] * 100  # dp[i] = i개를 터는 경우
dp[0] = food[0]
dp[1] = max(food[0], food[1])  # 1개를 터는 경우
for i in range(2, n):
    dp[i] = max(dp[i-2]+food[i], dp[i-1])

print(dp[n-1])
