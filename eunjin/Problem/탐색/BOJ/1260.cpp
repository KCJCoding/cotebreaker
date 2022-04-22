#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 1001

std::vector<int> graph[MAX];
bool visited[MAX] = {false, };
int n, m, v;

void reset()
{
	for (int i = 0; i <= n; i++)
		visited[i] = false;
}

void dfs(int v)
{
	// 현재 노드를 방문 처리
	visited[v] = true;
	std::cout << v << ' ';
	// 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for (int i = 0; i < graph[v].size(); i++)
	{
		int y = graph[v][i];
		if (!visited[y])
			dfs(y);
	}
}

void bfs(int v)
{
	std::queue<int> q;
	int tmp1, tmp2;

	q.push(v); //맨 처음 노드 push
	while (!q.empty()) // queue가 비지 않은 경우 반복
	{
		tmp1 = q.front();
		q.pop();
		visited[tmp1] = true; // pop 후 방문 처리
		std::cout << tmp1 << ' ';

		for (int i = 0; i < graph[tmp1].size(); i++) //인접한 노드 확인
		{
			tmp2 = graph[tmp1][i];
			if (!visited[tmp2]) //방문 하지 않았다면
			{
				q.push(tmp2); // queue에 넣고 방문 처리
				visited[tmp2] = true;
			}
		}
	}
}


int main()
{
	int tmp1, tmp2;

	std::cin >> n >> m >> v;

	for (int i = 0; i < m; i++)
	{
		std::cin >> tmp1 >> tmp2;
		graph[tmp1].push_back(tmp2);
		graph[tmp2].push_back(tmp1);
	}
	
	for (int i = 0; i <= n; i++) //정점 번확 작은 것을 먼저 방문하기 위해 정렬 
		std::sort(graph[i].begin(), graph[i].end());
	
	dfs(v);
	std::cout << "\n";

	reset(); //재 탐색을 위해 초기화 

	bfs(v);

	return 0;
}