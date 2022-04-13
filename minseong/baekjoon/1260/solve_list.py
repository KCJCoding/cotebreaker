def solve():
    N, M, V = map(int, input().split())
    graph = [list() for n in range(N+1)]

    for m in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for sub_graph in graph:
        sub_graph.sort()

    print_list(dfs(graph, [V]))
    print_list(bfs(graph, [V]))


def dfs(graph, discovered=None):
    v = discovered[-1]

    for node in graph[v]:
        if node not in discovered:
            discovered.append(node)
            discovered = dfs(graph, discovered)

    return discovered


def bfs(graph, discovered=None):
    v = discovered[0]
    queue_list = [v]

    while True:
        if len(queue_list) <= 0:
            break

        element = queue_list[0]
        queue_list = queue_list[1:]

        for node in graph[element]:
            if node not in discovered:
                queue_list.append(node)
                discovered.append(node)

    return discovered


def print_list(list):
    for element in list:
        print(element, end=" ")
    print("", end="\n")


if __name__ == '__main__':
    solve()