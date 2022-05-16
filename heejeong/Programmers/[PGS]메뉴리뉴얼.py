from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for num in course:  # 2 3 4 순
        order_list = []
        for order in orders:
            order = sorted(order)  # 입출력예3의 경우 때문에 정렬해주어야 함.
            # 각각의 조합 - append와 extend의 차이
            order_list.extend(list(combinations(order, num)))

        cnt = Counter(order_list)
        if cnt:  # 프로그래머스에서 max() 에러 때문에 추가해줌.
            if max(cnt.values()) >= 2:
                for key, value in cnt.items():
                    if value == max(cnt.values()):
                        answer.append("".join(key))

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
