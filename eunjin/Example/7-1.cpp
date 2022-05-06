//순차탐색
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> arr;

int sequential_search(int n, std::vector<std::string> arr, std::string target)
{
	for (int i = 0; i < n; i++)
	{
		if (arr[i] == target)
			return i + 1;
	}
	return -1;
}

int main()
{
	int n;
	std::string tmp, target;

	std::cout << "생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요. \n";
	std::cin >> n >> target;
	std::cout << "앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.\n";
	for (int i = 0; i < n; i++)
	{
		std::cin >> tmp;
		arr.push_back(tmp);
	}

	std::cout << sequential_search(n, arr, target);

	return 0;
}