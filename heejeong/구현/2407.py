from itertools import combinations

n, m = map(int, input().split())
top, bottom = 1, 1
for i in range(1, n+1):
    top *= i
for j in range(1, m+1):
    bottom *= j
for k in range(1, n-m+1):
    bottom *= k
print(top/bottom)
