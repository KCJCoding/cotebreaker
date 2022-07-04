'''
(x1, y1, x2, y2) : x1행 y1열부터 x2행 y2열까지의 영역에 해당하는 직사각형에서 
테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전.
row:세로 길이, column: 가로 길이
아무회전도 하지 않았을 때, i행 j열에 있는 숫자는 ((i-1)*columns+j)
'''


def solution(rows, columns, queries):
    answer = []
    data = [[[] for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            data[i][j] = (i)*columns + j + 1
    print(data)  # 확인용 - 나중에 삭제

    for query in queries:
        query = [x-1 for x in query]
        tmp = data[query[0]][query[1]]
        small = tmp

        # left
        for i in range(query[0]+1, query[2]+1):
            data[i-1][query[1]] = data[i][query[1]]
            small = min(small, data[i][query[1]])  # 다른 방향으로 이동해야 하는 값
        # bottom
        for i in range(query[1]+1, query[3]+1):
            data[query[2]][i-1] = data[query[2]][i]
            small = min(small, data[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            data[i+1][query[3]] = data[i][query[3]]
            small = min(small, data[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            data[query[0]][i+1] = data[query[0]][i]
            small = min(small, data[query[0]][i])
        data[query[0]][query[1]+1] = tmp

        answer.append(small)

    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, columns, queries))
