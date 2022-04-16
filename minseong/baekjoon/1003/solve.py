global dp


def solve():
    global dp
    T = int(input())
    test_cases = list()

    for t in range(T):
        test_cases.append(int(input()))

    for n in test_cases:
        dp = [0, 1]
        dp_fibonacci(n)
        if n == 0:
            count_zero = 1
        else:
            count_zero = dp[n-1]
        count_one = dp[n]
        print(f"{count_zero} {count_one}")


def dp_fibonacci(n):
    global dp
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        for i in range(2, n+1):
            if i == len(dp):
                dp.append(0)
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


if __name__ == '__main__':
    solve()
