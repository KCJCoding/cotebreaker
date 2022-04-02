n, k = map(int, input().split())

won = []
count = 0

for i in range(n):
    won.append(int(input()))

wons = sorted(won, reverse=True)

for i in range(n):
    if k == 0:
        break
    if k < wons[i]:
        continue
    count += k // wons[i]
    k = k % wons[i]

print(count)
