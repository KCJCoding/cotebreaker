n, m, k = map(int, input().split())  # n:개수, m:횟수, k:연속최대횟수
data = list(map(int, input().split()))

data = sorted(data, reverse=True)

data = data[0:2]

cnt_m = 0
result = 0
while True:
    for _ in range(3):
        result += data[0]
        cnt_m += 1
        if cnt_m == m:
            break
    result += data[1]
    cnt_m += 1

    if cnt_m == m:
        break
print(result)
