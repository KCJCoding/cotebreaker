'''
큐 구현 후, 입력으로 주어지는 명령 처리
큐 : First In First Out
'''
from collections import deque
import sys
input = sys.stdin.readline  # 시간초과 때문에 추가해줌
N = int(input())  # 명령의 수
q = deque()
for _ in range(N):
    info = list(input().split())
    if info[0] == 'push':
        q.append(info[1])

    elif info[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            num = q.popleft()
            print(num)
    elif info[0] == 'size':
        print(len(q))
    elif info[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif info[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif info[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
