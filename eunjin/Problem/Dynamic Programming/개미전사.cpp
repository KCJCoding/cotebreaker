#include <iostream>
#include <vector>
#include <algorithm>

int N;
int d[100];
std::vector<int> arr;
int main()
{
	int tmp;

	std::cin >> N; //N 입력
	for (int i = 0; i < N; i++) //식량정보 입력받기 
	{
		std::cin >> tmp;
		arr.push_back(tmp);
	}
	d[0] = arr[0]; //0 번째 값
	d[1] = arr[1]; //1 번째 값
	
	//d[1] = std::max(arr[0], arr[1]]) 이렇게 안해줘도 어차피 1 번째 들어가면 되지 않을까..? 
	
	for (int i = 2; i < N; i++)
	{
		d[i] = std::max(d[i - 1], d[i - 2] + arr[i]); //이전 값을 가져오는 것이 나은지, -2 번째 값에서 현재 값을 더한 것이 더 큰지
	}

	std::cout << d[N - 1]; //배열이 0부터 시작했으므로 -1 해줘야 함 
	return 0;
}