'''
[참고]
https://leedakyeong.tistory.com/135#comment16270807
'''
import math


def solution(w, h):
    # w와 h의 최대공약수를 주기로 점을 지남. 그 사이 지나는 사각형의 개수는 최대공약수
    answer = 1

    answer = w*h - (w+h-math.gcd(w, h))

    return answer
