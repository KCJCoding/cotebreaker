#회의실 배정 - 최대 사용할 수 있는 회의의 수 : 빨리 끝나는 회의 순서대로 정렬
n = int(input()) #회의의 수
data = []
cnt = 0
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
data.sort()
data.sort(key=lambda x:x[1]) #끝나는시간 기준 정렬

last = 0

for i, j in data:
    if i >= last:
        cnt += 1
        last = j
print(cnt)