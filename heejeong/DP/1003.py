'''
DP로 피보나치 함수 구현
0이 출력되는 횟수와 1이 출력되는 횟수 구하기
- f(n)의 0호출횟수, 1호출횟수 = f(n-1)0호출횟수, 1호출횟수 + f(n-2)0호출횟수, 1호출횟수
'''

'''
def fibo(n):
    global cnt0, cnt1
    if n == 0:
        cnt0 += 1
        return 0
    elif n == 1:
        cnt1 += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
'''

cnt0 = [1, 0, 1]  # 각 인덱스의 0호출 횟수
cnt1 = [0, 1, 1]  # 1호출 횟수

# bottom-up


def fibo(num):
    if num >= len(cnt0):
        for i in range(len(cnt0), num+1):
            cnt0.append(cnt0[i-1]+cnt0[i-2])
            cnt1.append(cnt1[i-1]+cnt1[i-2])
    print(cnt0[num], cnt1[num])


t = int(input())  # 테스트케이스
for _ in range(t):
    fibo(int(input()))
