'''
01타일
- 길이가 N인 이진 수열만들기
- 1 하나만으로 이루어진 타일, 혹은 0 두개로 이루어진 타일 만 가능
- N이 주어졌을 때 만들 수 있는 모든 가짓수 세기.
- 예를 들어 n = 5일 때, n=4일 때_타일1 붙인거 + n=3일 떼_타일00붙인 거
'''
n = int(input())
dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])

# 리스트에 저장할 때, 너무 큰 수를 넣으면 메모리초과 문제 발생.
# 반복문 안에서 수시로 나머지 연산을 해줘야 메모리초과가 발생하지 않음.
# 값이 int 값을 초과하게 되어서 n = 1000000일 경우 엄청나게 많은 메모리를 차지하게 됨.