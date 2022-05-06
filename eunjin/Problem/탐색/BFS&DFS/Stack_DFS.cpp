//재귀 호출이 아닌 stack 을 이용해서 DFS 구현 
#include <iostream>
#include <stack>
#include <vector>

std::vector<int> graph[9];
bool visited[9] = {false, };
std::stack<int> s;

void dfs(int start)
{
	s.push(start); //탐색 시작 노드
	visited[start] = true;
	std::cout << start << ' ';
	int x, y;

	while (!s.empty())
	{
		x = s.top();
		s.pop();
		for (int i = 0; i < graph[x].size(); i++)
		{
			y = graph[x][i];
			if (!visited[y]) //방문하지 않았다면 
			{
				s.push(y); //스택에 push 
				visited[y] = true; //방문 처리
				std::cout << y << ' ';
				break;
			}
		}
	}
}

int main()
{
	std::stack<int> s;

	// 노드 1에 연결된 노드 정보 저장
	graph[1].push_back(2);
	graph[1].push_back(3);
	graph[1].push_back(8);

	// 노드 2에 연결된 노드 정보 저장
	graph[2].push_back(1);
	graph[2].push_back(7);

	// 노드 3에 연결된 노드 정보 저장
	graph[3].push_back(1);
	graph[3].push_back(4);
	graph[3].push_back(5);

	// 노드 4에 연결된 노드 정보 저장
	graph[4].push_back(3);
	graph[4].push_back(5);

	// 노드 5에 연결된 노드 정보 저장
	graph[5].push_back(3);
	graph[5].push_back(4);

	// 노드 6에 연결된 노드 정보 저장
	graph[6].push_back(7);

	// 노드 7에 연결된 노드 정보 저장
	graph[7].push_back(2);
	graph[7].push_back(6);
	graph[7].push_back(8);

	// 노드 8에 연결된 노드 정보 저장
	graph[8].push_back(1);
	graph[8].push_back(7);

	for (int i = 1; i < 9; i++) //그래프가 분리 된 경우가 있으므로 재귀 사용
	{
		if (!visited[i]) //현재 노드를 방문하지 않았다면 
		{
			dfs(i);
		}
	}

	return 0;
}