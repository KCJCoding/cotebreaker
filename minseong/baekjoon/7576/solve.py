def solve():
    M, N = map(int, input().split())
    graph = make_graph(N)
    discovered = scan_grown(graph)
    print("(graph)")
    for subgraph in graph:
        print(subgraph)

    print(f"discovered_bef: {discovered}")
    grown_graph, discovered, date = bfs(graph, discovered)
    #grown_graph, discovered, date = dfs(graph, discovered, date=-1)
    print("(grown_graph)")
    for subgraph in grown_graph:
        print(subgraph)

    print(f"discovered_aft: {discovered}")
    print(f"date: {date}")

    if is_all_grown(grown_graph):
        return date
    else:
        return -1


def make_graph(N):
    graph = list()

    for n in range(N):
        graph.append([int(grown) for grown in input().split()])

    return graph


def scan_grown(graph):
    discovered = list()

    for i, subgraph in enumerate(graph):
        for j, grown in enumerate(subgraph):
            if grown == 1:
                discovered.append((i, j))

    return discovered


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


def dfs(graph, discovered, date):
    i, j = discovered[-1]
    xy_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for x, y in xy_list:
        dx = i + x
        dy = j + y

        if 0 <= dx < len(graph) and 0 <= dy < len(graph[0]):
            if graph[dx][dy] == 0:
                graph[dx][dy] = 1
                discovered.append((dx, dy))
                graph, discovered, date = dfs(graph, discovered, date)
                date += 1

    return graph, discovered, date


def is_all_grown(graph):
    for subgraph in graph:
        if 0 in subgraph:
            return False

    return True


if __name__ == '__main__':
    print(solve())
