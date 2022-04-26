#include <iostream>
#include <vector>
#include <algorithm>

int binary_search(std::vector<int>& arr, int start, int end, int target)
{ 
	int middle;

	if (start > end)
		return -1;
	middle = (start + end) / 2; //end의 중간이 아니라 start 와 end가 늘 바뀌기 때문에 주의
	if (arr[middle] == target)
		return middle;
	else if (arr[middle] < target) //target이 더 큼 -> middle 이후 범위 탐색 
		return binary_search(arr, middle + 1, end, target);
	return binary_search(arr, start, middle - 1, target); //target이 더 작음 -> middle 이전 범위 탐색 
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
	std::sort(arr.begin(), arr.end());

	int result = binary_search(arr, 0, n - 1, target) + 1;

	if (result == 0)
		std::cout << "원소가 존재하지 않음 \n";
	else
		std::cout << result; 
	
	return 0;
}