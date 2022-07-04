#include <iostream>
#include <cmath>

#define MAX 15

using namespace std;

int queen[MAX];
int N, answer = 0;

bool check(int x)
{
	for (int i = 0; i < x; i++)
	{
		if (queen[x] == queen[i] || x - i == abs(queen[x] - queen[i])) //같은 열이나 대각선에 있는 경우
			return false; 
	}
	return true;
}

void nqueen(int x)
{
	if (x == N) //한 번 다 놨다면 경우의 수 증가 
	{
		answer++;
		return;
	}
	else
	{
		for (int i = 0; i < N; i++)
		{
			queen[x] = i; //현재 행 배열 위치에 i (열) 놓기 -> 퀸 놓기
			if (check(x)) //현재 행 열 위치가 괜찮다면 다음 행에 퀸 놓기 (가지치기)
			{
				nqueen(x + 1); // 다음 행 퀸 놓기 
			}
		}
	}

}

int main()
{
	cin >> N;
	nqueen(0);
	cout << answer;
	return 0;
}