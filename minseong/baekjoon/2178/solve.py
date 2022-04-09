def solve():
    N, M = map(int, input().split(' '))
    graph = make_graph(N)
    traverse = bfs
    #dfs(graph, [(0, 0)], N-1, M-1)
    graph = traverse(graph, N-1, M-1)
    print(graph[N-1][M-1])


def make_graph(N):
    graph = list()

    for n in range(N):
        graph.append([int(node) for node in input()])

    return graph


def dfs(graph, discovered, N, M):
    xy_list = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    i, j = discovered[-1]
    graph[i][j] = 0

    if i == N and j == M:
        #print(discovered)
        print(len(discovered))

    for x, y in xy_list:
        index_x = i + x
        index_y = j + y

        if 0 <= index_x <= N and 0 <= index_y <= M:
            if graph[index_x][index_y] == 1:
                discovered.append((index_x, index_y))
                discovered = dfs(graph, discovered, N, M)

    return discovered


def bfs(graph, N, M):
    queue_list = [(0, 0)]
    xy_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        i, j = queue_list[0]
        queue_list = queue_list[1:]

        if i == N and j == M:
            break

        for x, y in xy_list:
            dx = i + x
            dy = j + y

            if 0 <= dx <= N and 0 <= dy <= M:
                if graph[dx][dy] == 1:
                    queue_list.append((dx, dy))
                    graph[dx][dy] = graph[i][j] + 1

        if len(queue_list) <= 0:
            break

    return graph


if __name__ == '__main__':
    solve()
