def solve():
    N, M, V = map(int, input().split())
    graph = [[0] * (N + 1) for n in range(N + 1)]

    for m in range(M):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1

    print_list(dfs(graph, [V]))
    print_list(bfs(graph, [V]))


def dfs(graph, discovered=None):
    v = discovered[-1]

    for i, node in enumerate(graph[v]):
        if node == 1 and i not in discovered:
            discovered.append(i)
            discovered = dfs(graph, discovered)

    return discovered


def bfs(graph, discovered=None):
    while True:
        if len(graph) <= 0:
            break

        sub_graph = graph[0]
        graph = graph[1:]
        for i, edge in enumerate(sub_graph):
            if edge == 1:
                sub_graph[i] = 0

                if i not in discovered:
                    discovered.append(i)

    return discovered


def print_list(list):
    for element in list:
        print(element, end=" ")
    print("", end="\n")


if __name__ == '__main__':
    solve()
