def solve():
    N = int(input())
    withdrawal_times = [time for time in map(int, input().split())]
    withdrawal_times.sort(key=lambda x: x)
    cumulative_time = 0
    spend_times = []

    for time in withdrawal_times:
        cumulative_time += time
        spend_times.append(cumulative_time)

    total_time = 0
    for time in spend_times:
        total_time += time

    return total_time


if __name__ == '__main__':
    print(solve())
