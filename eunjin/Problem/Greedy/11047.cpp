#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	int n, k, result = 0;
	std::cin >> n >> k;
	std::vector<int> coin(n);
	for (int i = 0; i < n; i++)
		std::cin >> coin[i];
	std::sort(coin.begin(), coin.end(), std::greater<int>()); //내림차순 정렬
	
	for (auto a : coin)
	{
		result += k / a;
		k %= a;
	}
	std::cout << result;

	return 0;
}