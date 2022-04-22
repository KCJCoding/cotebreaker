#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

#define MAX 101

int n, m;
std::vector<int> computer[101]; //벡터가 아니라 배열로 바꿀수 있을 것 같다,,, 
bool visited[101] = {false, };

int main()
{
	int tmp1, tmp2, result;
	std::queue<int> q;

	result = 0;
	std::cin >> n >> m;

	for(int i = 1; i <= m; i++)
	{
		std::cin >> tmp1 >> tmp2;
		computer[tmp1].push_back(tmp2);
		computer[tmp2].push_back(tmp1);
	}
	// for (int i = 1; i <= m; i++)
	// 	std::sort(computer[i].begin(), computer[i].end());

	q.push(1);
	visited[1] = true;

	while(!q.empty())
	{
		tmp1 = q.front();
		visited[tmp1] = true;
		q.pop();
		for (int i = 0; i < computer[tmp1].size(); i++)
		{
			tmp2 = computer[tmp1][i];
			if(!visited[tmp2])
			{
				q.push(tmp2);
				visited[tmp2] = true;
				result++;
			}
		}
	}

	std::cout << result;
	return 0;
}