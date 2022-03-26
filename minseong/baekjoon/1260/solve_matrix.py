def solve():
    N, M, V = map(int, input().split())
    graph = [[0] * (N + 1) for n in range(N + 1)]

    for m in range(M):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1

    dfs(graph, [V])
    #bfs(graph, V)


def dfs(graph, discovered=None):
    v = discovered[-1]
    print(v)

    for i, node in enumerate(graph[v]):
        if node == 1 and i not in discovered:
            discovered.append(i)
            dfs(graph, discovered)


def bfs(graph, V):
    pass


if __name__ == '__main__':
    print(solve())
