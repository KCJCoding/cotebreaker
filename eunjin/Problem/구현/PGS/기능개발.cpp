#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) 
{
    vector<int> answer;
	queue<int> q;
	for (int i = 0; i < progresses.size(); i++)
	{
		int rest = 100 - progresses[i];
		int days = rest / speeds[i];
		if (rest % speeds[i] != 0)
			days++;
		q.push(days);
	}
	int cnt;
	while(!q.empty())
	{
		cnt = 1;
		int front = q.front(); //제일 처음 배포되어야 하는 날짜
		q.pop();
		
		while((!q.empty()) && (q.front() <= front)) //같이 배포될 수 있는 작업 수 구하기 -> 현재 front 날짜보다 더 작은 경우
		{
			q.pop();
			cnt++;
		}
		answer.push_back(cnt); 
	}
    return answer;
}

int main()
{
	vector<int> progresses, sppeds;
	progresses.push_back(93);
	progresses.push_back(30);
	progresses.push_back(55);

	sppeds.push_back(1);
	sppeds.push_back(30);
	sppeds.push_back(5);

	vector<int> answer = solution(progresses, sppeds);
	for (auto a : answer)
		std::cout << a << '\n';
	return 0;
}