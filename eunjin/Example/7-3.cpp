#include <iostream>
#include <vector>
#include <algorithm>

int binary_search(std::vector<int> &arr, int start, int end, int target)
{
	int middle;

	while (start <= end)
	{
		middle = (start + end) / 2;
		if (arr[middle] == target)
			return middle;
		else if (arr[middle] > target)
			end = middle + 1;
		else 
			start = middle - 1;
	}
	return -1;
}

int main() //예제 main 코드
{
	int n, target, tmp;
	std::cin >> n >> target;
	std::vector<int> arr;

	for (int i = 0; i < n; i++)
	{
		std::cin >> tmp;
		arr.push_back(tmp);
	}
	//std::sort(arr.begin(), arr.end());

	int result = binary_search(arr, 0, n - 1, target) + 1; //0부터 시작했으므로 

	if (result == 0)
		std::cout << "원소가 존재하지 않음 \n";
	else
		std::cout << result;

	return 0;
}