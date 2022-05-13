#include <iostream>

int fibo(int n)
{
	if (n == 1 || n == 2)
		return 1;
	return fibo(n - 1) + fibo(n - 2);
}

int main()
{
	std::cout << fibo(5) << "\n";
	return 0;
}