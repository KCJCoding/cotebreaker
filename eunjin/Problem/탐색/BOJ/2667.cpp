#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 25

int N, house_cnt; 
std::vector<int> result; //각 단지 내 수를 담을 벡터 (벡터 사이즈 : 총 단지 수)
int map[MAX][MAX];
bool visited[MAX][MAX];

void dfs(int x, int y)
{
	if (x < 0 || x >= N || y < 0 || y >= N) //현재 노드가 맵을 벗어났다면 종료 
		return;
	if (map[x][y] == 1 && visited[x][y] == false) //현재 위치가 집이 있고 방문하지 않았다면 방문 처리 후 상하좌우 방문 
	{
		house_cnt++; 		  
		visited[x][y] = true; //방문 처리
		//상 하 좌 우 노드 확인 
		dfs(x - 1, y);
		dfs(x + 1, y);
		dfs(x, y - 1);
		dfs(x, y + 1);
	}
}

int main()
{
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			scanf("%1d", &map[i][j]);
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (map[i][j] == 1 && visited[i][j] == false) //현재 맵 위치가 1이고 이전에 방문하지 않았을 경우
			{
				house_cnt = 0; //단지 내의 수 초기화 
				dfs(i, j);
				result.push_back(house_cnt); //탐색 후 push 
			}
		}
	}
	std::sort(result.begin(), result.end());

	std::cout << result.size() << "\n"; //총 단지 수 출력 
	for (int i = 0; i < result.size(); i++)
		std::cout << result[i] << "\n"; //단지 내 수 출력 

	return 0;
}