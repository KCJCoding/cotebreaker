def solve():
    coin_kind, expected_value = map(int, input().split())
    assert 1 <= coin_kind <= 10
    assert 1 <= expected_value <= 100000000

    coin_list = [int(input()) for kind in range(coin_kind)]
    coin_list.reverse()
    value = expected_value
    count = 0

    for coin in coin_list:
        if value > coin:
            quotient, value = divmod(value, coin)
            count += quotient

        assert value >= 0

        if value == 0:
            break

    return count


if __name__ == '__main__':
    print(solve())
