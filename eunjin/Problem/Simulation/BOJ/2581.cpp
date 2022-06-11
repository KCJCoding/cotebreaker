#include <iostream>

int main()
{
	int N, M, sum = 0, min = -1, tmp = 0;
	std::cin >> N >> M;

	for (int i = N; i <= M; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			if (i % j == 0)
				tmp++;
		}
		if (tmp == 2) //소수라면 1과 자기 자신 2개 뿐일 것
		{
			if (min == -1) //맨 처음의 소수가 제일 작은 값이므로 해당 i 값 저장
				min = i;
			sum += i;
		}
		tmp = 0;
	}
	if (min == -1)
		std::cout << -1 << '\n';
	else
		std::cout << sum << '\n' << min << '\n';

	return 0;
}