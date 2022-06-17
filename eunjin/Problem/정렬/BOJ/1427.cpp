#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
	std::string str;
	std::vector<char> v;

	std::cin >> str;
	//std::sort(str.begin(), str.end(), greater<char>()); -> 간단한 방법 

	std::reverse(str.begin(), str.end());
	for (int i = 0; i < str.length(); i++)
	{
		v.push_back(str[i]);
	}
	std::sort(v.begin(), v.end(), std::greater<int>());


	for (auto a : v)
		std::cout << a;

	return 0;
}