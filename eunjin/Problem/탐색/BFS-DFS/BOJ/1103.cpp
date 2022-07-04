#include <iostream>
#include <algorithm>

int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

char map[50][50];
int visited[50][50] = {{-1, }};

int N, M;

using namespace std;

int dfs(int x, int y)
{
	if (x < 0 || y < 0 || x >= N || y >= M || map[x][y] == 'H')
		return 0;

	int answer = 0;
	if (visited[x][y] == -1) //아직 방문하지 않았다면 
	{
		visited[x][y] = 0; // 방문 처리
		for (int i = 0; i < 4; i++)
		{
			int nx = x + (dx[i] * (map[x][y] - '0'));
			int ny = y + (dy[i] * (map[x][y] - '0'));
			answer = max(answer, dfs(nx, ny) + 1);
		}
		visited[x][y] = answer; //현재 값을 visited에 작성. 이전에 왔다 간 최적의 값
		return answer; 
	}
	else if (visited[x][y] == 0) //cycle
	{
		cout << -1;
		exit(0);
	}
	else
		return visited[x][y]; //black으로 처리 
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
			visited[i][j] = -1;
		}
	}
	cout << dfs(0, 0);
	return 0;
}