

# Check near nodes (NSWE) -> Make edge -> Trace graph from never traced nodes


def solve():
    N = int(input())
    strict_map = None
    assert 5 <= N <= 25

    for n in range(N):
        strict_map = [int(value) for value in input()]

    assert isinstance(strict_map, list)

    graph, nodes = make_graph(strict_map)

    while True:
        i, j = nodes[0]

        if len(nodes) > 0:
            nodes = nodes[1:]
        else:
            break


def make_graph(strict_map):
    N = len(strict_map)
    graph = [[0] * N for n in range(N)]
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
