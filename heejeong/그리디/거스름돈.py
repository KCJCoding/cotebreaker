n = 1260

won = [500, 100, 50, 10]
ans = 0
while n > 0:
    for coin in won:
        ans += n // coin
        n %= coin


print(ans)
