'''
사전식으로 가능성 있는 암호 모두 출력 - 최소 1개의 모음, 최소 두개의 자음
'''
from itertools import combinations
L, C = map(int, input().split())
data = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
data.sort()
answer = []
result = list(combinations(data, L))
# print(result)
# print(data)

for i in range(len(result)):
    cnt_v, cnt_c = 0, 0
    for j in range(L):
        if result[i][j] in vowels:
            cnt_v += 1
        else:
            cnt_c += 1
    if cnt_v >= 1 and cnt_c >= 2:
        # password = result[i][0] + result[i][1] + result[i][2] + result[i][3]
        answer.append(''.join(result[i]))
set(answer)
for ans in answer:
    print(ans)