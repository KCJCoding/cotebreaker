#include <iostream>
#include <string>
#include <algorithm>

int main()
{
	std::string str1, str2;
	std::cin >> str1 >> str2;

	std::reverse(str1.begin(), str1.end());
	std::reverse(str2.begin(), str2.end());

	int num1 = atoi(str1.c_str());
	int num2 = atoi(str2.c_str());

	if (num1 > num2)
		std::cout << num1;
	else
		std::cout << num2;
	
	return 0;
}