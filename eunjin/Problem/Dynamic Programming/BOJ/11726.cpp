#include <iostream>

int N;
int dp[1001] = {0,};
int main()
{
	std::cin >> N;
	dp[1] = 1; //2x1 타입은 딱 하나(기둥처럼 생긴,,)만 놓을 수 있음
	dp[2] = 2; //2x2 타입은 두 개를 놓을 수 있음 (2x1 두 개, 1x2 두 개)

	for (int i = 3; i <= N; i++) //2x1, 2x2는 이미 정해져 있으므로 2x3부터 채우기 
	{
		dp[i] = dp[i - 1] + dp[i - 2]; //어떤 타일을 놓든 이전에 타일을 배치한 경우의 수가 됨
		dp[i] %= 10007;
	}
	std::cout << dp[N];

	return 0;
}