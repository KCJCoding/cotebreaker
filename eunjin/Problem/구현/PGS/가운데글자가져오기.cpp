#include <string>
#include <vector>
#include <iostream>

//using namespace std;

std::string solution(std::string s)
{
	std::string answer = "";

	int len = s.length();
	if (len % 2 == 0)
	{
		// answer+=s[(len/2) - 1];
		// answer+=s[(len/2)];

		//substr 사용 (되도록이면 substr을 사용하자)
		answer = s.substr((len/2) - 1, 2);
	}
	else
	{
		answer = s[len/2];
	}

	return answer;
}


int main()
{
	std::cout << solution("abcde") << '\n';
	std::cout << solution("qwer") << '\n';

	return 0;
}