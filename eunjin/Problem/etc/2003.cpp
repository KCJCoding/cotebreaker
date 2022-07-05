#include <algorithm>
#include <iostream>

using namespace std;

int N, M;
int A[10000];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// scanf("%d%d",&N,&M);
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		// scanf("%d", &A[i]);
		cin >> A[i];

	}
	int answer = 0;
	int start = 0;
	int end = 0;
	int sum = 0;

	while (end <= N)
	{
		if (sum >= M) //M을 넘었다면 -> start를 움직여준다 
			sum -= A[start++];
		else if (sum < M) //M을 넘지 못함 -> end를 움직여준다 
			sum += A[end++]; 
		if (sum == M) //M이 딱 되었다면 경우의 수 추가
			answer++;
	}
	cout << answer;
	return 0;
}