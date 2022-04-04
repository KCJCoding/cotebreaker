n = int(input())

graph = []
house = []
count = 0
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            house.append(count)
            count = 0

house.sort()
print(result)
for i in range(len(house)):
    print(house[i])
