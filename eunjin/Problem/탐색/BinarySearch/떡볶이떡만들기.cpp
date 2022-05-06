//이분탐색
#include <iostream>
#include <vector>
#include <algorithm>

int N, M;
std::vector<int> arr;

int main()
{
	std::cin >> N >> M;
	int tmp, start, middle, end, result;
	long long int total; 

	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		arr.push_back(tmp);
	}

	//std::sort(arr.begin(), arr.end()); 정렬 하면 결과 안나옴 
	start = 0;
	end = 1e9;

	while(start <= end)
	{
		total = 0;
		middle = (start + end) / 2;
		for (int a : arr)
		{
			if (a > middle)
				total += (a - middle);
		}
		if (total < M) // M이 더 큰 경우 -> 왼쪽 부분 탐색 (더 자르기)
			end = middle - 1;
		else //M보다 더 큰 경우 -> 오른쪽 부분 탐색 (덜 자르기)
		{
			result = middle; 
			start = middle + 1;
		}
	}
	std::cout << result << "\n";

	return 0;
}