#include <iostream>

int d[100] = {0,}; //전역변수

int main()
{
	d[1] = 1;
	d[2] = 1;
	int n = 99;
	for (int i = 3; i < n + 1; i++) //상향식 다이나믹 프로그래밍 
	{
		d[i] = d[i - 1] + d[i - 2];
	}
	std::cout << d[5];
	return 0;
}