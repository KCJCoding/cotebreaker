n = int(input())
p = list(map(int, input().split()))
time = []

p.sort()
time.append(p[0])
sum = time[0]

for i in range(1, n, 1):
    time.append(time[i-1] + p[i])
    sum += time[i]

print(sum)
