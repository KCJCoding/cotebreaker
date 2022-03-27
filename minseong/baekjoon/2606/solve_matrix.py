def solve():
    pc_quantity = int(input()) + 1  # to ignore index 0
    edges_len = int(input())
    start_node = 1
    graph = from_adjmatrix(pc_quantity, edges_len)

    infected_count = track_warm(graph, [start_node]) - 1  # to ignore 1st pc

    return infected_count


def from_adjmatrix(node_size, edge_size):
    graph = [[0] * node_size for i in range(node_size)]

    for _ in range(edge_size):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1

    return graph


def track_warm(graph, discovered=None):
    # dfs_result = dfs(graph, discovered)
    bfs_result = bfs(graph, discovered)

    return len(bfs_result)


def dfs(graph, discovered=None):
    last_node = discovered[-1]

    for i, edge in enumerate(graph[last_node]):
        if edge == 1 and i not in discovered:
            discovered.append(i)
            discovered = dfs(graph, discovered)

    return discovered


def bfs(graph, discovered=None):
    start_node = discovered[0]
    task_queue = [start_node]

    while True:
        if len(task_queue) <= 0:
            break

        task = task_queue[0]

        for i, edge in enumerate(graph[task]):
            if edge == 1 and i not in discovered:
                discovered.append(i)
                task_queue.append(i)

        task_queue = task_queue[1:]

    return discovered


if __name__ == '__main__':
    print(solve())
