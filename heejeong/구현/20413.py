'''
MVP 다이아몬드(EASY)
한 번 달성한 MVP등급은 줄어들지 않는다. 
다이아몬드는 최대 500까지
'''
N = int(input())  # 게임을 플레이한 개월 수
sgpd = list(map(int, input().split()))  # 길이 4
mvp = input()
result = 0
prev = 0

for i in range(N):
    if mvp[i] == 'B':
        result += sgpd[0] - 1 - prev
        prev = sgpd[0] - 1 - prev
    elif mvp[i] == 'S':
        result += sgpd[1] - 1 - prev
        prev = sgpd[1] - 1 - prev
    elif mvp[i] == 'G':
        result += sgpd[2] - 1 - prev
        prev = sgpd[2] - 1 - prev
    elif mvp[i] == 'P':
        result += sgpd[3] - 1 - prev
        prev = sgpd[3] - 1 - prev
    else:
        result += sgpd[3]
        prev = sgpd[3]
print(result)

# 초기 풀이
result = []
prev = 0
now = 0
for i in range(N):
    if mvp[i] == 'B':
        if i == 0:
            now = sgpd[0] - 1
            prev = now
            result.append(now)
        else:
            now = (sgpd[0]-1) - prev
            result.append(now)
            prev = now
    elif mvp[i] == 'S':
        if i == 0:
            now = sgpd[1] - 1
            prev = now
            result.append(now)
        else:
            now = (sgpd[1]-1) - prev
            result.append(now)
            prev = now
    elif mvp[i] == 'G':
        if i == 0:
            now = sgpd[2] - 1
            prev = now
            result.append(now)
        else:
            now = (sgpd[2]-1) - prev
            result.append(now)
            prev = now
    elif mvp[i] == 'P':
        if i == 0:
            now = sgpd[3] - 1
            prev = now
            result.append(now)
        else:
            now = (sgpd[3]-1) - prev
            result.append(now)
            prev = now
    else:  # 다이아몬드
        if i == 0:
            now = 500
            prev = now
            result.append(now)
        else:
            now = 500
            result.append(now)

print(sum(result))
