#include <iostream>

int N;
int d[1001];
int main()
{
	std::cin >> N;
	d[1] = 1; //2x1 타일만 놓을 수 있어서 한 가지
	d[2] = 3; //(2x1 두 개), (1x2 두 개), (2x2 한 개) 타일 놓을 수 있어서 세 가지
	for (int i = 3; i <= N; i++)
	{
		d[i] = (d[i - 1] + (d[i - 2] * 2)) % 796796;
		//i - 1 인 경우 : i - 1 앞의 내용에 2x1 기둥 하나만 놓은 경우. 
		//i - 2 인 경우 : i - 2 앞의 내용에 1x2 두 개 / 2x2 한 개 놓은 경우 -> 2 곱함
	}
	std::cout << d[N] << '\n';
	return 0;
}