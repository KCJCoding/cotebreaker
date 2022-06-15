#include <iostream>
#include <vector>

int N;
std::pair<int,int> tree[26];

void pre(char cur) //루트 -> 왼 -> 오
{
	if (cur == '.')
		return;
	std::cout << cur; //현재 루트 먼저
	pre(tree[cur - 'A'].first); //왼쪽
	pre(tree[cur - 'A'].second); //오른쪽
}

void in (char cur) //왼 -> 루트 -> 오
{
	if (cur == '.')
		return;
	in(tree[cur - 'A'].first); //왼쪽
	std::cout << cur; //루트
	in(tree[cur - 'A'].second); //오른쪽
}

void post(char cur) //왼 -> 오 -> 루트
{
	if (cur == '.')
		return;
	post(tree[cur - 'A'].first); //왼쪽
	post(tree[cur - 'A'].second); //오른쪽
	std::cout << cur; //루트
}


int main()
{
	char node, left, right;
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	std::cin >> N;
	
	for (int i = 0; i < N; i++)
	{
		std::cin >> node >> left >> right;
		tree[node - 'A'] = {left, right};
	}

	pre('A');
	std::cout << '\n';
	in('A');
	std::cout << '\n';
	post('A');
	return 0;
}