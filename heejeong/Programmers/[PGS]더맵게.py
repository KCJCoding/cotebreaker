'''
스코빌 지수가 K미만인 경우만 섞어주기.
섞어주면 2개 -> 1개
'''
import heapq


def solution(scoville, K):
    answer = 0  # 횟수 계산
    heapq.heapify(scoville)  # 배열을 힙으로 바꿔주기

    while True:
        firstMin = heapq.heappop(scoville)
        if firstMin > K:
            break
        if len(scoville) == 0:
            return -1  # 예외처리
        secondMin = heapq.heappop(scoville)
        result = firstMin + (secondMin * 2)
        heapq.heappush(scoville, result)
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
