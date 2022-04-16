def solve():
    M, N = map(int, input().split())
    graph, discovered = make_graph(N)
    grown_graph, discovered, date = bfs(graph, discovered)

    if is_all_grown(grown_graph):
        return date
    else:
        return -1


def make_graph(N):
    graph = list()
    discovered = list()

    for i in range(N):
        subgraph = list()
        for j, grown in enumerate(input().split()):
            int_grown = int(grown)
            subgraph.append(int_grown)
            if int_grown == 1:
                discovered.append((i, j))

        graph.append(subgraph)

    return graph, discovered


def bfs(graph, discovered):
    queue_list = discovered
    xy_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while True:
        i, j = queue_list[0]
        queue_list = queue_list[1:]

        for x, y in xy_list:
            dx = i + x
            dy = j + y

            if 0 <= dx < len(graph) and 0 <= dy < len(graph[0]):
                if graph[dx][dy] == 0:
                    graph[dx][dy] = graph[i][j] + 1
                    queue_list.append((dx, dy))

        if len(queue_list) < 1:
            date = graph[i][j] - 1
            break

    return graph, discovered, date


def is_all_grown(graph):
    for subgraph in graph:
        if 0 in subgraph:
            return False

    return True


if __name__ == '__main__':
    print(solve())
