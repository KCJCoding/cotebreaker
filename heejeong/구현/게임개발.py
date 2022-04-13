'''
NxM 크기의 직사각형. 각각의 칸은 육지 or 바다
(A, B) A:북쪽으로부터 떨어진 칸의 개수, B: 서쪽으로부터 떨어진 칸의 개수 - 행, 열
상하좌우로 움직이기 가능, 바다(1)로 되어 있는 공간은 갈 수 없음.
방문한 칸의 수 출력.
'''

dx = [-1, 0, 1, 0] #북 동 남 서  0 1 2 3
dy = [0, 1, 0, -1] 

#print(visit)
#print(board)

def move(x, y, d):
    global cnt
    if board[x][y] == 0:
        board[x][y] = 2
        cnt += 1
    for _ in range(4):
        d_left = (d+3) % 4 #바라보는 방향의 왼쪽방향
        nx = x + dx[d_left]
        ny = y + dy[d_left]
        if board[nx][ny] == 0:
            move(nx, ny, d_left)
            return #이동종료시 바로 리턴
        d = d_left #청소불가능한 경우 바라보는 방향만 업데이트해주기

    #4방향 모두 이동 불가일 때 후진할 수 있는지 확인
    d_left = (d+2) % 4
    nx = x + dx[d_left]
    ny = y + dy[d_left]
    if board[nx][ny] == 1: #후진 위치가 바다면 이동 종료, 이동할 수 있으면 다음 좌표방향입력
        return
    move(nx, ny, d)

    
n, m = map(int, input().split()) #세로 가로
x, y, d = map(int, input().split()) #현재 위치, 방향
board = [] #맵 정보
cnt = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

move(x, y, d)
print(cnt)
