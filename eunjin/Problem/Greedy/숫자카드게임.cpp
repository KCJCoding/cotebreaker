#include <iostream>

int main()
{
	int n, m, tmp, min_value, result = 0;
	std::cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		min_value = 10001;
		for (int j = 0; j < m; j++)
		{
			std::cin >> tmp;
			min_value = std::min(min_value, tmp); //행마다 최소 값 저장
		}
		result = std::max(result, min_value); //최소 값과 현재 결과 값 중 큰 값 저장
	}

	std::cout << result;

	return 0;
}