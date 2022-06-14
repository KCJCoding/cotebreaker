#include <queue>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0, index = 0, cnt = 1;
	queue<pair<int, int>> print_list;
	priority_queue<int> pq;
	for (auto a : priorities)
	{
		print_list.push({a, index++});
		pq.push(a);
	}
	while (!print_list.empty())
	{
		int priority = print_list.front().first;
		index = print_list.front().second;

		if (priority >= pq.top())
		{
			if (index == location) 
				return cnt;
			cnt++; //location이 아니라면 출력 횟수 증가
			print_list.pop(); //출력 -> pop 
			pq.pop(); //출력하면 해당 우선순위도 삭제해주기 
		}
		else //우선순위가 더 낮음
		{
			print_list.push(print_list.front());
			print_list.pop();
		}
	}
    return answer;
}

int main()
{
	vector<int> p;
	p.push_back(1);
	p.push_back(1);
	p.push_back(9);
	p.push_back(1);
	p.push_back(1);
	p.push_back(1);
	
	cout << solution(p, 0);

	return 0;
}