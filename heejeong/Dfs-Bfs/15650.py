# 재귀함수는 실행하면 밑의 코드를 읽지 않고 재귀함수가 끝날 때까지 실행됨.
# 그 깊이를 끝까지 탐색하고 나서야 종료됨.
N, M = map(int, input().split())

result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return 
    for i in range(1, N+1): # ex) 1 2 3 4
        if i not in result:
            if len(result) == 0 or i > result[-1]:
                result.append(i)
            else:
                continue
            dfs()
            result.pop()
        
dfs()
            
'''
4 2
1 2
1 3
1 4
2 3
2 4
3 4
'''