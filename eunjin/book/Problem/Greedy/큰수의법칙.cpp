#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	int n, m, k, tmp = 0, result = 0;

	std::cin >> n >> m >> k;

	std::vector<int> arr(n);

	for (int i = 0; i < n; i++)
		std::cin >> arr[i];

	std::sort(arr.begin(), arr.end(), std::greater<int>()); //내림차순 정렬

	for (int i = 0; i < m; i++)
	{
		if (tmp < k)
		{
			result += arr[0]; //제일 큰 수 
			tmp++;
			continue;
		}
		result += arr[1]; //두 번째로 큰 수
		tmp = 0;
	}
	std::cout << result;
	
	return 0;
}