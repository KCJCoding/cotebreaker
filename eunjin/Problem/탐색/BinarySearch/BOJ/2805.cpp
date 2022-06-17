#include <iostream>
#include <vector>
#include <algorithm>

int N, M, answer = 0;
std::vector<int> tree;

void search(int start, int end)
{
	long long int total = 0; //int를 해도 상관은 없을 것 같다 
	int  middle;

	while (start <= end)
	{
		total = 0;
		middle = (start + end) / 2;

		for (auto a : tree)
		{
			if (a > middle)
			{
				total += a - middle; //middle 값은 빼야 함 : 나무 길이에서 middle 만큼 잘랐으므로 
			}
		}

		if (total >= M) //자른 나무가 입력 M 보다 더 큼 -> 오른쪽 더 탐색 (나무를 덜 잘라서 높이를 더 설정하도록)
		{
			start = middle + 1;
			answer = middle; //현재 값 저장 (최대일 수도 있으니)
		}
		
		else //작음 -> 왼쪽으로 옮겨서 더 자를 수 있도록 
		{
			end = middle - 1;
		}
	}
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	int tmp;

	std::cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		tree.push_back(tmp);
	}

	std::sort(tree.begin(), tree.end());
	search(0, tree[tree.size() - 1]);

	std::cout << answer;

	return 0;
}