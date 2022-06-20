#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main()
{
	int N, tmp;
	std::cin >> N;
	std::priority_queue<int> pq;
	
	while (N--)
	{
		std::cin >> tmp;
		if (tmp != 0)
		{
			pq.push(tmp);
		}
		else
		{
			if (!pq.empty())
			{
				std::cout << pq.top() << '\n';
				pq.pop();
			}
			else
			{
				std::cout << 0 << '\n';
			}
		}
	}

	return 0;
}