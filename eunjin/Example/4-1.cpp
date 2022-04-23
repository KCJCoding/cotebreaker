#include <iostream>
#include <string>

char move[4] = {'U', 'D', 'R', 'L'};
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

// dx[0] dy[0] = U (위로 한 칸)
// dx[1] dy[1] = D (아래로 한 칸)
// dx[2] dy[2] = R (오른 쪽으로 한 칸)
// dx[3] dy[3] = L (왼 쪽으로 한 칸)


int main()
{
	int n, x = 1, y = 1, nx, ny;
	std::string str;
	char cmd;

	std::cin >> n;
	std::cin.ignore(); //버퍼 비우기
	std::getline(std::cin, str);

	for (int i = 0; i < str.size(); i++)
	{
		nx = -1, ny = -1;
		cmd = str[i];
		for (int j = 0; j < 4; j++)
		{
			if (cmd == move[j])
			{
				nx = x + dx[j];
				ny = y + dy[j];
			}
		}
		if (nx < 1 || ny < 1 || nx > n || ny > n)
			continue;
		//이동
		x = nx; 
		y = ny;
	}

	std::cout << x << ' ' << y << "\n";
	
	return 0;
}