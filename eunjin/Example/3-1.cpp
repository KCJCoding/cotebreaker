#include <iostream>

int main()
{
	int n = 1260, count = 0;
	int coin[4] = {500, 100, 50, 10};

	for (auto a : coin)
	{
		count += n / a;
		n %= a;
	}

	std::cout << count << "\n";
}