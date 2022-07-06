#include <queue>
#include <algorithm>
#include <iostream>
#pragma warning(disable:4996)
using namespace std;


int main()
{
	int N, mid = 0, tmpN;
	scanf("%d", &N);

	tmpN = N;
	priority_queue<int, vector<int>, greater<int>> max_heap; //오름차순
	priority_queue<int, vector<int>> min_heap; //내림차순

	while (N--)
	{
		int tmp;

		scanf("%d", &tmp);
		if (N == tmpN - 1) //맨 처음 값은 그대로 중간 값이 됨 
		{
			mid = tmp;
			printf("%d\n", mid);
			continue;
		}

		if (tmp >= mid) //현재 중간 값 보다 크면 최대 힙 
		{
			max_heap.push(tmp);
		}
		else
			min_heap.push(tmp); //그렇지 않으면 최소 힙
		
		if (max_heap.size() - 2 == min_heap.size()) //최대 힙에서 값을 빼와서 중간 값을 재설정 해야 하는 경우
		//최대 힙과 최소 힙의 사이즈가 같거나 최대 힙이 하나 더 많은 것 까진 허용
		{
			min_heap.push(mid); //현재 중간 값은 최소 힙으로 (더 큰 값이 중간값이 되어야 함)
			mid = max_heap.top(); //최대 힙에서 가장 작은 값 가져오기 
			max_heap.pop();
		}
		else if (min_heap.size() > max_heap.size()) //최소 힙에서 값을 빼와서 중간 값으로 설정해야 하는 경우
		{
			max_heap.push(mid); //현재 중간 값은 최대 힙으로 (더 작은 값이 중간 값이 되어야 함)
			mid = min_heap.top(); //최소 힙에서 가장 큰 값 가져오기 
			min_heap.pop();
		}
		printf("%d\n", mid);

	}

	return 0;
}