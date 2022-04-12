def solution(numbers, target):
    super = [0]
    k = 0
    for i in numbers:
        k += 1
        sub = []
        for j in super:
            sub.append(j+i)  # 덧셈 - j는 super에 있던 결과값, i는 numbers원소
            sub.append(j-i)  # 뺄셈
        super = sub  # 결과를 super에 넣어주기.
        print(k, "번째 super", super)

    return super.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3

result = solution(numbers, target)
print(result)
