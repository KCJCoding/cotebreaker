#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	int n, time, result;

	result = 1;
	std::cin >> n;
	std::vector<std::pair<int, int> > meet_time(n);

	for (int i = 0; i < n; i++)
		std::cin >> meet_time[i].second >> meet_time[i].first;
		//std::cin >> meet_time[i].first >> meet_time[i].second;
	
	std::sort(meet_time.begin(), meet_time.end()); //pair는 정렬 될 때 first를 기준으로 정렬하기 때문에 종료 시간을 first 로 받음

	time = meet_time[0].first; //제일 첫 번째 회의의 종료시간 
	for (int i = 1; i < meet_time.size(); i++)
	{
		if (time <= meet_time[i].second) //이전 회의의 종료 시간보다 시작 시간이 크거나 같다면 예약
		{
			result++;
			time = meet_time[i].first; //종료시간으로 설정 
		}
	}
	
	std::cout << result;
	return 0;
}