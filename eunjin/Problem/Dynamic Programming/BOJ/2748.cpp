#include <iostream>

using namespace std;

long long dp[90] = {0,};

long long fib(int n)
{
	if (n <= 1)
		return dp[n];
	else if (dp[n] == 0)
		dp[n] = fib(n - 1) + fib(n - 2);
	return dp[n];
}

int main()
{
	int N;
	dp[0] = 0;
	dp[1] = 1;
	cin >> N;
	cout << fib(N);
	return 0;
}