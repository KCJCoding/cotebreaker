'''
숨바꼭질 - 동생을 찾는 가장 빠른 시간 출력
- 걷기 or 순간이동
'''
from collections import deque


def bfs():
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()
        if now == k:
            return
        for i in (now-1, now+1, now*2):
            if 0 <= i < 100001 and dp[i] == 0:  # dp[i] == 0이면 방문안된 것.
                dp[i] = dp[now]+1  # i까지의이동횟수저장
                q.append(i)


n, k = map(int, input().split())
dp = [0]*100001
bfs()
print(dp[k])
