#include <iostream>

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	int N, tmp;
	int count[10001] = {0,};

	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> tmp;
		count[tmp]++;
	}

	for(int i = 0; i < 10001; i++) //배열 인덱스가 크지 않으면 출력하지 않고 넘어갈 것이므로 10001까지 인 듯,, 
        for(int j = 0; j < count[i]; j++) //0부터 올라가면서 갯수로 출력하기 
            std::cout << i << '\n';

	return 0;
}