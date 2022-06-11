#include <iostream>
#include <string>

int main()
{
	int T, len, result, tmp;
	std::string str;
	
	std::cin >> T;
	while (T--)
	{
		result = 0;
		tmp = 0;
		std::cin >> str;
		len = str.length();
		for (int i = 0; i < len; i++)
		{
			if (str[i - 1] == 'O' && i > 0)
			{
				tmp++;
			}
			else
				tmp = 0;
			if (str[i] == 'O')
			{
				result++;
				result+=tmp;
			}

		}
		std::cout << result << '\n';
	}

	return 0;
}
