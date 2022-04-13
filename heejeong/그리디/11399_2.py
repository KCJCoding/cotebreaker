#ATM - 각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값
#사람은 1번 ~ N번

n = int(input()) #사람의 수
time = list(map(int, input().split())) #각 사람이 돈을 인출하는 데 걸리는 시간

time.sort()
for i in range(1, n):
    time[i] += time[i-1]
print(sum(time))