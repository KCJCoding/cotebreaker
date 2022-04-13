n, m = map(int, input().split())  # 행 과 열
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
min_data = []
for i in range(n):
    min_data.append(min(data[i]))
print(max(min_data))
