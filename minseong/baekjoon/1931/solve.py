def solve():
    N = int(input())
    time_list = []

    for n in range(N):
        start_time, end_time = map(int, input().split())

        if in_time(start_time, end_time, time_list):
            time_list.append((start_time, end_time))
        else:
            continue

    return len(time_list)


def in_time(start, end, time_list):
    if len(time_list) == 0:
        return True

    for time in time_list:
        if time[0] <= start < time[-1]:
            return False
        if time[0] < end <= time[-1]:
            return False

    return True


if __name__ == '__main__':
    print(solve())
