#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	int tmp, sum = 0;
	std::vector<int> height;
	for (int i = 0; i < 9; i++)
	{
		std::cin >> tmp;
		sum += tmp;
		height.push_back(tmp);
	}

	std::sort(height.begin(), height.end());

	//이중포문으로 한 명씩 검사. [0,1], [0,2], [0,3]...를 sum에서 빼서 검사 
	for(int i = 0; i < 9; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if (sum - (height[i] + height[j]) == 100) //두 난쟁이 키 빼면 100
			{
				for (int k = 0; k < 9; k++)
				{
					if (k == i || k == j) //현재 i와 j 가 난쟁이가 아니므로 출력 제외
						continue;
					std::cout << height[k] << '\n';
				}
				return 0;
			}
		}
	}

	return 0;
}