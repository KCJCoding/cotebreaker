#include <iostream>
#include <algorithm>

int X;
int d[30001] = {0, };

int main()
{
	std::cin >> X;
	for (int i = 2; i <= X; i++)
	{
		d[i] = d[i - 1] + 1;
		if (i % 2 == 0)
			d[i] = std::min(d[i], d[i / 2] + 1); // 1을 뺀 횟수와 2로 나는 횟수 중 최적의 횟수 (이때 2로 나눈 횟수에서 +1 해줘야 함)
		if (i % 3 == 0)
			d[i] = std::min(d[i], d[i / 3] + 1); // 1을 뺀 횟수와 3로 나는 횟수 중 최적의 횟수 (이때 3로 나눈 횟수에서 +1 해줘야 함)
		if (i % 5 == 0)
			d[i] = std::min(d[i], d[i / 5] + 1); // 1을 뺀 횟수와 5로 나는 횟수 중 최적의 횟수 (이때 5로 나눈 횟수에서 +1 해줘야 함)
	}
	std::cout << d[X] << '\n';
	return 0;
}