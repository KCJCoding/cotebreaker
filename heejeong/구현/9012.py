T = int(input())
result = []
ans = []
for _ in range(T):
    data = input()
    for i in range(len(data)):
        if data[i] == '(':
            result.append(data[i])
            # print("넣은 후", result)
        else:
            # print("result 크기", len(result))
            if len(result) == 0:
                result.append(data[i])
            else:
                if result[-1] == '(':
                    # print("제거")
                    result.pop() # 마지막 요소 제거

    if len(result) != 0:
        ans.append('NO')
    else:
        ans.append('YES')
    result = []

for tc in range(T):
    print(ans[tc])