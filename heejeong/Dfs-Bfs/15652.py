# 15651번 오름차순으로
N, M = map(int, input().split())

result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if len(result) == 0 or i >= result[-1]:
            result.append(i)
        else:
            continue
        dfs()
        result.pop()


dfs()