#include <iostream>

int graph[1000][1000]; //최대 그래프 크기 1000 x 1000 
int n, m;

bool dfs(int x, int y)
{
	if (x <= -1 || x >= n || y <= -1 || y >= m)
		return false;
	if (graph[x][y] == 0) //현재 노드를 방문한 적이 없다면 
	{
		graph[x][y] = 1; //방문으로 처리 후 상 하 좌 우 dfs 함수 실행 
		dfs(x - 1, y);
		dfs(x + 1, y);
		dfs(x, y - 1);
		dfs(x, y +1);
		return true;
	}
	return false;
}

int main()
{
	int result;

	result = 0;
	std::cin >> n >> m; //n, m 입력

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%1d", &graph[i][j]); //std::cin으로 입력받아도 되지만 한 줄을 입력받아서 구별해야 하므로 scanf 사용
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (!graph[i][j]) //이미 방문한 노드라면 다시 방문할 필요 없음
			{
				if (dfs(i, j))
					result++;
			}
		}
	}

	std::cout << result;

	return 0;

}