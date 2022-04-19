'''
신나는 함수 만들기
- 재귀, dp로 만들기
- 세 수가 20보다 크면 모두 20리턴하므로 dp크기를 20으로 정하기
'''


def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:  # 값이 이미 존재하는 경우 보내줘야 함.
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1)+w(a, b-1, c-1)-w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)
    return dp[a][b][c]


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]


while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print(f'w({x}, {y}, {z}) = {w(x, y, z)}')
