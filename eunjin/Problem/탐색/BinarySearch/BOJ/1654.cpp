#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);

	//int로 작성할 경우 랜선 길이에 따라 오버플로우가 날 확률이 높다. 
	unsigned int N, K, tmp, start, end, middle, result, total, maxi;
	std::vector<unsigned int> arr;

	result = 0, maxi = 0; //입력 된 랜선 중 가장 긴 랜선을 구하기 위함
	std::cin >> K >> N;
	for (int i = 0; i < K; i++)
	{
		std::cin >> tmp;
		arr.push_back(tmp);
		maxi = std::max(maxi, arr[i]);
	}
	start = 1, end = maxi; //1 ~ 가장 긴 랜선 사이의 값으로 범위 설정 
	//INT_MAX로 할 경우 오버플로우가 발생할 확률이 높다. 

	while (start <= end)
	{
		middle = (start + end) / 2; 
		total = 0;

		for (int a : arr)
		{
			total += a / middle; //중간 값으로 나눈 값 누적 
		}

		if (total < N) //N이 더 크다면 자를 수 있는 길이를 줄여서 더 많이 자를 수 있도록 한다. (왼쪽으로 이동)
			end = middle - 1;
		else //N이 같거나 작다면 자를 수 있는 길이를 늘려서 덜 자르도록 함 (오른쪽으로 이동) -> 더 길게 자를 수 있도록 
		{
			start = middle + 1;
			result = std::max(result, middle); //현재 값을 최적으로 저장 
		}
	}

	std::cout << result;

	return 0;
}