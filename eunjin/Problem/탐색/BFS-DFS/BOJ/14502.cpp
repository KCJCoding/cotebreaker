#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

int N, M, cnt = 3;

int map[10][10];
int map2[10][10];

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

vector<int>answer;

void bfs()
{
	int tmp = 0; 

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
			map2[i][j] = map[i][j]; //map2에 현재 맵 복사 
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map2[i][j] == 2) //현재 좌표에 바이러스가 있다면 
			{
				queue<pair<int, int>> q; //좌표이므로 pair 생성 

				q.push({i, j});

				while (!q.empty()) //큐가 비지 않을 때 까지 
				{
					int cur_x = (q.front()).first;
					int cur_y = (q.front()).second;
					q.pop();

					for (int k = 0; k < 4; k++) //주변을 돌면서 바이러스가 있는지 확인하기 
					{
						int nx = cur_x + dx[k];
						int ny = cur_y + dy[k];
						if (nx <= -1 || nx >= N || ny <= -1 || ny >= M) //맵을 벗어나면 안됨 
							continue;
						if (map2[nx][ny] == 0) //상하좌우가 0이라면 바이러스 감염 (아니라면 넘어감. 이전에 2로 적는 실수를,,, )
						{
							q.push({nx, ny});
							map2[nx][ny] = 2;
						}
					}
				}
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map2[i][j] == 0) //바이러스 전파 후 안전지역 갯수를 셈 
				tmp++;
		}
	}

	answer.push_back(tmp); //answer 벡터에 넣어서 max_element로 최대 안전지역을 구함 
}

void Search() //벽을 놓을 모든 가능성 찾기 (조합)
{
	if (cnt == 0)
	{
		return bfs(); //벽을 다 세웠다면 bfs 함수 호출
	}
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 0)
			{
				cnt--;
				map[i][j] = 1; //벽 세우기
				Search();	//다른 조합 찾으러 가기 
				cnt++;		//다 하고 돌아왔다면 다시 벽 0으로 만들기 
				map[i][j] = 0;
			}
		}
	}
}

int main()
{
	int tmp;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	memset(map, -1, sizeof(map));
	memset(map2, -1, sizeof(map2));

	cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
		}
	}

	Search();

	int max = *max_element(answer.begin(), answer.end());
	cout << max;
	
	return 0;
}