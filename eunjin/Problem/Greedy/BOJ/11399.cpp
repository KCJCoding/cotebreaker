#include <iostream>
#include <vector>
#include <algorithm>


int main()
{
	int n, result = 0;

	std::cin >> n;
	std::vector<int> p(n);

	for(int i = 0; i < n; i++)
		std::cin >> p[i];

	std::sort(p.begin(), p.end());
	
	for (int i = 0; i < p.size(); i++)
	{
		for (int j = 0; j <= i; j++)
			result += p[j];
	}

	std::cout << result;
	return 0;
}