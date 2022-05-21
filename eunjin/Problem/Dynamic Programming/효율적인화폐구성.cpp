#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

int N, M;
std::vector<int> coin;
int main()
{
	int tmp;

	std::cin >> N >> M; 
	for (int i = 0; i < tmp; i++)
	{
		std::cin >> tmp;
		coin.push_back(tmp);
	}
	std::vector<int> d(M + 1, std::numeric_limits<int>::max());
	d[0] = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = coin[i]; j <= M; j++)
		{
			if (d[j - coin[i]] != std::numeric_limits<int>::max())
				d[j] = std::min(d[j], d[j - coin[i]] + 1);
		}
	}
	if (d[M] == std::numeric_limits<int>::max())
		std::cout << -1;
	else
		std::cout << d[M];
	return 0;
}