#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

std::vector<int>graph[9];
bool visited[9] = {false,};

void bfs(int n)
{
	std::queue<int> q;
	int tmp1, tmp2;

	q.push(n); //맨 처음 노드 push 

	while(!q.empty()) //queue가 비지 않은 경우 반복 
	{
		tmp1 = q.front();
		q.pop();
		visited[tmp1] = true; //pop 후 방문 처리
		std::cout << tmp1 << " ";

		for (int i = 0; i < graph[tmp1].size(); i++) //인접한 노드 확인 
		{
			tmp2 = graph[tmp1][i];
			if(!visited[tmp2]) //방문 하지 않았다면
			{
				q.push(tmp2); //queue에 넣고 방문 처리 
				visited[tmp2] = true;
			}
		}
	}
}


int main(void)
{
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

	bfs(1);

	return 0;
}