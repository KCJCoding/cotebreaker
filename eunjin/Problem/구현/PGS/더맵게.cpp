#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
	priority_queue<int, vector<int>, greater<int>> pq; //오름차순으로 우선순위 큐 생성
	for (auto a : scoville)
		pq.push(a);
	
	while (pq.size() > 1 && pq.top() < K) 
	//pq안에 있는 값 들이 두 개 이상이여야 스코빌 지수를 만들 수 있음 && 맨 위에 있는 값이 K보다 작아야 함 
	{
		int min = pq.top(); //제일 위에 있는 것 -> 제일 작은 값
		pq.pop();
		// if (min >= K) //while 문에 있는 조건 
		// 	break;
		int min2 = pq.top();
		pq.pop();
		pq.push(min + (min2 * 2));
		answer++;
	}
	// if (pq.size() <= 1)	//-1이 나올 조건 : K를 만들 수 없을 떄 
	// 	return -1;
	if (pq.top() < K) //-1이 나오는 조건은 size가 1보다 작은 것도 있지만 제일 위에 있는 값이 K보다 작을 때 (어차피 size가 1보다 작으면 while문 끝남)
		return -1;
    return answer;
}
