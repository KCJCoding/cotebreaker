'''
빈칸 : 0
치킨집 : 2
집 : 1
(r, c) : r행 c열 (1부터 시작)
- 치킨거리 = 집과 가장 가까운 치킨집 사이의 거리
- 도시의 치키거리 = 모든 집의 치킨거리의 합
-> 도시의 치킨거리가 가장 작게 될지를 구하는 프로그램
-> 폐업시키지 않을 치킨집을 최대 M개 골랐을 대, 도시의 치킨거리의 최솟값
<생각1>
- 치킨집을 기준으로 치킨거리를 구한 후(최솟값) 
- 치킨거리를 오름차순 정렬 -> M개까지의 합 구하기.
- 최대 M개의 치킨집을 고르는 것.
'''
from itertools import combinations


def makeChickenLength(chi_x, chi_y):
    for k in range(len(house)):
        x, y = house[k]
        new_res = abs(x - chi_x) + abs(y - chi_y)
        chickenLength[x][y] = min(chickenLength[x][y], new_res)  # 최솟값으로 업데이트


N, M = map(int, input().split())  # 크기, 치킨집의 최대개수
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))


# 집과 치킨집의 위치 넣어주기.
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            house.append([i, j])
        elif data[i][j] == 2:
            chicken.append([i, j])

# 치킨집 M개를 고르는 경우
pickedChicken = list(combinations(chicken, M))
# print(len(pickedChicken))
# print(pickedChicken)

answer = []

for i in range(len(pickedChicken)):  # 모든 경우의 수에 대하여 해줌 - 각각의 경우에서의 도시치킨거리 저장하고 그 중 최솟값
    # 치킨거리 저장하는 리스트 - 각 경우의 수마다 초기화
    chickenLength = [[100] * N for _ in range(N)]

    for j in range(M):
        chi_pos = pickedChicken[i][j]
        makeChickenLength(chi_pos[0], chi_pos[1])

    final = []
    for i in range(N):
        for j in range(N):
            if chickenLength[i][j] != 100:
                final.append(chickenLength[i][j])
    #print("도시치킨거리", sum(final))
    answer.append(sum(final))

print(min(answer))
