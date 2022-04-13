#include <iostream>

int main()
{
	int n, k, result = 0;
	std::cin >> n >> k;

	while(n != 1)
	{
		if (n % k == 0)
		{
			n /= k;
			result++;
			continue;
		}
		n--;
		result++;
	}
	std::cout << result;

	return 0;
}