//이분탐색
#include <iostream>
#include <vector>
#include <algorithm>

int N, M;
std::vector<int> arr, target;

int binary_search(std::vector<int> arr, int start, int end, int target)
{
	int middle;

	while (start <= end)
	{
		middle = (start + end) / 2;
		if (arr[middle] == target)
			return middle;
		else if (arr[middle] > target)
			end = middle - 1;
		else
			start = middle + 1;
	}
	return -1;
}

int main()
{
	int tmp;
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		arr.push_back(tmp);
	}

	std::sort(arr.begin(), arr.end());

	std::cin >> M;

	for (int i = 0; i < M; i++)
	{
		std::cin >> tmp;
		target.push_back(tmp);
	}

	for (int i = 0; i < M; i++)
	{
		//해당 부품이 있는지 확인 
		if (binary_search(arr, 0, N - 1, target[i]) != -1) //arr 배열 최대를 검사해야 한다
			std::cout << "yes \n";
		else
			std::cout << "no \n";
	}

	return 0;
}