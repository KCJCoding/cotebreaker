#include <iostream>

int T;
long long fiboarr[50] = {0, 1, }; 

long long fibo(int N)
{
	if (N == 0 | N == 1)
		return fiboarr[N];
	else if (fiboarr[N] == 0) //아직 채우지 않았다면
		fiboarr[N] = fibo(N - 1) + fibo(N - 2);
	return fiboarr[N];
}
int main()
{
	int tmp;

	std::cin >> T;
	for (int i = 0; i < T; i++)
	{
		std::cin >> tmp;
		if (tmp == 0)
			std::cout << "1 0\n";
		else if (tmp == 1)
			std::cout << "0 1\n";
		else
			std::cout << fibo(tmp - 1) << ' ' << fibo(tmp) << '\n';
	}	

	return 0;
}