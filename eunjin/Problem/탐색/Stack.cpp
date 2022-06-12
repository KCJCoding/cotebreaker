#include <iostream>
#include <stack>

int main()
{
	std::stack<int> s;
	s.push(5);
	s.push(2);
	s.push(3);
	s.push(7);
	s.push(1);
	s.pop();
	s.push(4);

	while (!s.empty())
	{
		std::cout << s.top() << '\n';
		s.pop(); //출력하려면 무조건 top->pop 해야 함,,
	}
	return 0;
}