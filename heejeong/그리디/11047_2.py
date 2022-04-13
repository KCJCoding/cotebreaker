#K원을 만드는 데 필요한 동전의 최소개수 구하기

n, k = map(int, input().split()) #종류
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in range(n):
    cnt += k // coins[i]
    k %= coins[i]
print(cnt)