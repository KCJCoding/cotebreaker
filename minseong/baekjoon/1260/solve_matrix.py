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
    queue_list = [discovered[0]]

    while True:
        if len(queue_list) <= 0:
            break

        element = queue_list[0]
        queue_list = queue_list[1:]

        for i, edge in enumerate(graph[element]):
            if edge == 1 and i not in discovered:
                discovered.append(i)
                queue_list.append(i)

    return discovered


def print_list(list):
    for element in list:
        print(element, end=" ")
    print("", end="\n")


if __name__ == '__main__':
    solve()
