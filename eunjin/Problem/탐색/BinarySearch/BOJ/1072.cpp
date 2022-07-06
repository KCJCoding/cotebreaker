#include <iostream>
#include <algorithm>
#include <cmath>

#define MAX 1000000000

using namespace std;


int main()
{
	long long X, Y, Z, answer = 0;

	cin >> X >> Y;
	Z = (Y * 100) / X;

	if (Z == 100 || Z == 99)
	{
		cout << -1;
		return 0;
	}
	long long start = 0, end = MAX;
	while (start <= end) //이분탐색 
	{
		long long middle = (start + end) / 2;
		long long tmp = ((Y + middle) * 100) / (X + middle); //middle 만큼 이겼을 때의 승률

		if (tmp > Z)
		{
			answer = middle;
			end = middle - 1; 	//최소 게임수를 구하기 위해 middle - 1로 옮김 
		}
		else
		{
			start = middle + 1; //부족하므로 게임 수를 middle + 1로 늘림 
		}
	}
	cout << answer;
	return 0;
}
