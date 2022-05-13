#include <iostream>

int d[100] = {0, }; //전역변수 

int fibo(int n)
{
	if (n == 1 || n == 2)
		return 1;
	if (d[n] != 0) //이미 계산한 적 있다면 그대로 반환한다. 
		return d[n];
	d[n] = fibo(n - 1) + fibo(n - 2); //아직 계산하지 않았다면 점화식에 따라 피보나치 계산 
	return d[n];
}

int main()
{
	std::cout << fibo(10) << "\n";
	return 0;
}

