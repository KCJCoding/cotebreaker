'''
n가지 종류의 화폐
화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 m원이 되도록
- 풀이보고 풀었다.
- 가장 큰 화폐단위부터 처리하는 방식으로는 해결이 불가했다. 
- 적은 금액부터 큰 금액까지 차례대로 만들 수 있는 최소한의 화폐를 찾아야 함.
- 최소 화폐 개수를 dp테이블로 생성하고 화폐 단위별로 loop 돌면서 dp업데이트해주기
'''
n, m = map(int, input().split())  # n: 화폐종류,  m: 가치의 합
money = []
for _ in range(n):
    money.append(int(input()))

dp = [10001] * (m+1)  # 10001 : i-k를 만드는 방법이 없는 경우
dp[0] = 0

for i in range(n):  # 화폐 종류 개수 만큼
    for j in range(money[i], m+1):  # 화폐단위가 있는 수부터 차례대로 만들 수 있는 가지 수 조사
        if dp[j - money[i]] != 10001:
            dp[j] = min(dp[j], dp[j - money[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
