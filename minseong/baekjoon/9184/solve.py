global dp


def solve():
    global dp
    dp = [[[0] * 21]*21 for _ in range(21)]
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(w(a, b, c))


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        saved = dp[20][20][20]
        if saved == 0:
            dp[20][20][20] = w(20, 20, 20)
        return dp[20][20][20]
    elif a < b < c:
        saved = dp[a][b][c]
        if saved == 0:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        saved = dp[a][b][c]
        if saved == 0:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]


if __name__ == '__main__':
    solve()