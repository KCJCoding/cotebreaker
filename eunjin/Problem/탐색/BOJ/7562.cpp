#include <iostream>
#include <queue>
#include <algorithm>
#define MAX 300

int N, I;
int map[MAX][MAX];
bool visited[MAX][MAX];

//나이트 이동 방향 
int dx[8] = {2, 2, -2, -2, 1, -1, 1, -1};
int dy[8] = {-1, 1, -1, 1, 2, 2, -2, -2};

int bfs(std::pair<int, int> start, std::pair<int, int> end)
{
	int nx, ny, x, y;
	std::queue<std::pair<int, int> > q;

	q.push(start);
	while (!q.empty())
	{
		x = q.front().first;
		y = q.front().second;
		q.pop();
		visited[x][y] = true;

		// 현재 위치에서 8가지 방향으로의 위치 확인 
		for (int i = 0; i < 8; i++)
		{
			std::cout << "x : " << x << " y : " << y << "\n";
			std::cout << "nx : " << nx << " ny : " << ny << "\n";
			nx = x + dx[i];
			ny = y + dy[i];
			// 체스 공간 벗어난 경우 무시 
			if (nx < 0 || nx >= I || ny < 0 || ny >= I)
				continue;
			if (nx == end.first && ny == end.second)
				return map[nx][ny];
			// 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
			if (visited[nx][ny] == false)
			{
				map[nx][ny] = map[x][y] + 1;
				q.push(std::make_pair(nx, ny)); //이동한 위치 push -> 후에 그 위치 기준으로 다시 주변 노드 확인
			}
		}
	}
	return 0;
}

int main()
{
	std::pair<int, int> start;
	std::pair<int, int> end;
	int start_x, start_y, end_x, end_y;
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		memset(map, 0, sizeof(map));
		memset(visited, 0, sizeof(visited));
		std::cin >> I;
		std::cin >> start.first >> start.second;
		std::cin >> end.first >> end.second;
		std::cout << bfs(start, end) << "\n";
	}

	return 0;	
}