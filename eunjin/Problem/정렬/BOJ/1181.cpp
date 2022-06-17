#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

bool compare(const std::string &a, const std::string &b)
{
	if (a.length() == b.length()) //길이가 같은 경우에는 
		return a < b;			  //알파벳 순으로 정렬 
	return a.length() < b.length(); //기본적으로는 길이로 정렬 
}

int main()
{
	int N;
	std::string tmp;
	std::vector<std::string> str;
	
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		str.push_back(tmp);
	}

	std::sort(str.begin(), str.end());
	str.erase(std::unique(str.begin(), str.end()), str.end());
	std::sort(str.begin(), str.end(), compare);

	for (int i = 0; i < str.size(); i++)
	{
		std::cout << str[i] << '\n';
	}


	return 0;
}