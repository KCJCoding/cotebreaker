#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int N, M, tmp;
	std::vector<int> card;

	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		card.push_back(tmp);
	}
	std::sort(card.begin(), card.end());
	std::cin >> M;

	while (M--)
	{
		std::cin >> tmp;
		std::vector<int>::iterator a = std::lower_bound(card.begin(), card.end(), tmp);
		std::vector<int>::iterator b = std::upper_bound(card.begin(), card.end(), tmp);
		std::cout << b - a << " ";
	}

	return 0;
}