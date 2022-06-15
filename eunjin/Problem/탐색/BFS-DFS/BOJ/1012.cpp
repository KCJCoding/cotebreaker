#include <iostream>
#include <string.h> //memset 때문에 include 

int T, N, M, K;

int arr[50][50] = {0, };

bool dfs(int x, int y)
{
	if (x <= -1 || x >= N || y <= -1 || y >= M)
		return false;
	if (arr[x][y] == 1) //현재 노드가 1이라면 (배추가 있다면)
	{
		arr[x][y] = 2; //방문으로 처리 후 상 하 좌 우 dfs 함수 실행 (방문시 2로 작성)
		dfs(x - 1, y);
		dfs(x + 1, y);
		dfs(x, y - 1);
		dfs(x, y +1);

		return true; //상 하 좌 우를 다 돌았다면 (재귀로 주변 1을 모두 셌다면)
	}
	return false;
}

int main()
{
	int x, y, result;
	std::cin >> T;

	while(T--)
	{
		result = 0;
		std::cin >> N >> M >> K;
		memset(arr, 0, sizeof(arr)); //초기화
		for (int i = 0; i < K; i++)
		{
			std::cin >> x >> y;
			arr[x][y] = 1; //배추가 심어진 좌표는 1로 작성 
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (arr[i][j] == 1) //배추로 심어진 곳만 방문. 이 때 이미 방문했다면 방문할 필요 없음 (1만 방문)
				{
					if (dfs(i, j))
						result++;
				}
			}
		}
		std::cout << result << '\n';
	}

	return 0;
}