#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL); //왕창빨라짐 

	int N, tmp;
	std::vector<int> v;
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		v.push_back(tmp);
	}
	std::sort(v.begin(), v.end());
	for (auto a : v)
		std::cout << a << '\n';

	return 0;
}