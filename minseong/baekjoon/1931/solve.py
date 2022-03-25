def solve():
    N = int(input())
    assert 1 <= N <= 100000

    time_list = []
    for n in range(N):
        start_time, end_time = map(int, input().split())
        time_list.append((start_time, end_time))

    time_list.sort(key=lambda x: x[0])
    time_list.sort(key=lambda x: x[1])

    count = 1
    end = time_list[0][1]
    for i in range(1, N):
        if end <= time_list[i][0]:
            end = time_list[i][1]
            count += 1

    return count


if __name__ == '__main__':
    print(solve())
