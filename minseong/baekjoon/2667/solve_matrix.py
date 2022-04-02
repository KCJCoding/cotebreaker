def solve():
    N = int(input())
    strict_map = list()
    assert 5 <= N <= 25

    for n in range(N):
        strict_map.append([int(value) for value in input()])

    assert isinstance(strict_map, list)

    graph, nodes = make_graph(strict_map)
    count_list = list()

    while True:
        if len(nodes) <= 0:
            break

        node = nodes[0]
        count, nodes = bfs(graph, [node], nodes)
        count_list.append(count)

    count_list.sort()
    print(len(count_list))
    for count in count_list:
        print(count)


def bfs(graph, discovered=None, nodes=None):
    start_node = discovered[0]
    nodes.remove(start_node)
    task_list = [start_node]

    while True:
        task = task_list[0]

        for index, edge in enumerate(graph[task]):
            if edge == 1 and index not in discovered:
                task_list.append(index)
                discovered.append(index)
                nodes.remove(index)

        if len(task_list) <= 1:
            break
        else:
            task_list = task_list[1:]

    return len(discovered), nodes


def make_graph(strict_map):
    N = len(strict_map)
    graph = [[0] * (N * N) for n in range((N * N))]
    nodes = list()

    for i in range(len(strict_map)):
        for j in range(len(strict_map[i])):
            apartment = strict_map[i][j]

            if apartment == 1:
                node_number = i * N + j
                nodes.append(node_number)

                for neighbor in find_neighbors(strict_map, i, j):
                    n1 = node_number
                    n2 = neighbor
                    graph[n1][n2] = 1
                    graph[n2][n1] = 1

    return graph, nodes


def find_neighbors(strict_map, i, j):
    N = len(strict_map)
    neighbors = list()

    for neighbor_i, neighbor_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if check_neighbor(strict_map, neighbor_i, neighbor_j):
            num_neighbor = neighbor_i * N + neighbor_j
            neighbors.append(num_neighbor)

    return neighbors


def check_neighbor(strict_map, i, j):
    N = len(strict_map)

    if 0 <= i < N and 0 <= j < N:
        neighbor = strict_map[i][j]

        if neighbor == 1:
            return True

    return False


if __name__ == '__main__':
    solve()
