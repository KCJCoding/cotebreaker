#include <iostream>
#include <queue>

int main()
{
	std::queue<int> q;
	q.push(5);
	q.push(3);
	q.push(7);

	q.pop();
	q.push(1);
	q.push(4);
	q.pop();

	while (!q.empty())
	{
		std::cout << q.front() << '\n';
		q.pop();
	}

	return 0;
}