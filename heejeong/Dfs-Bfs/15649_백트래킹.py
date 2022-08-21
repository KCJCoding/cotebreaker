from itertools import combinations
N, M = map(int, input().split()) # N까지의 자연수 중에서 중복 없이 M개를 고른 수열

result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result))) #출력하면 해당 dfs 재귀 끝남
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop() # dfs 재귀 끝났으면 
            
dfs()