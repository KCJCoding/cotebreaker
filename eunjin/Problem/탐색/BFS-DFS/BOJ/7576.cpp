#include <iostream>
#include <queue>
#define MAX 1001

int N, M, result = 0;

int map[MAX][MAX] = {0,};
bool visited[MAX][MAX] = {false,};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

std::queue<std::pair<int, int> > q;
void bfs()
{
	int x, y, nx, ny;
	while (!q.empty())
	{
		y = q.front().first;
		x = q.front().second;
		visited[y][x] = true;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx < 0 || ny < 0 || nx >= N || ny >= M) //맵을 벗어난 경우 
				continue;
			if (map[ny][nx] == 0 && visited[ny][nx] == false) //익지 않은 경우
			{
				map[ny][nx] = map[y][x] + 1; //해당 맵에 날을 추가
				q.push(std::make_pair(ny, nx));
				visited[ny][nx] = true;
			}
		}
	}
}

int main()
{
	std::cin >> N >> M;
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			std::cin >> map[i][j];
			if (map[i][j] == 1) //익은 토마토가 있으면 queue에 push
				q.push(std::make_pair(i, j)); // 1인 경우 해당 위치 push
		}
	}
	bfs();

	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (map[i][j] == 0)
			{
				std::cout << -1;
				return 0;
			}
			if (result < map[i][j])
				result = map[i][j];
		}
	}
	std::cout << result - 1;
	return 0;
}