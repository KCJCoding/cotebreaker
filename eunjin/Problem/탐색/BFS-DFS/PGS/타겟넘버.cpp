#include <string>
#include <vector>

int answer = 0;

void dfs(std::vector<int> numbers, int target, int sum, int index)
{
	if (index == numbers.size()) //끝에 도달 한 경우 (모든 인덱스 다 검사한 경우)
	{
		if (sum == target) //합계가 target과 일치하면 경우의 수 증가 
			answer++;
		return;
	}
	dfs(numbers, target, sum + numbers[index], index + 1); //다음 인덱스와 더하기
	dfs(numbers, target, sum - numbers[index], index + 1); //다음 인덱스에서 빼기 
}

int solution(std::vector<int> numbers, int target)
{
	dfs(numbers, target, 0, 0); //맨 처음부터 시작 
	return answer;
}

#include <iostream>

int main()
{
	int target = 3;
	std::vector<int> numbers;
	numbers.push_back(1);
	numbers.push_back(1);
	numbers.push_back(1);
	numbers.push_back(1);
	numbers.push_back(1);

	std::cout << solution(numbers, target) << "\n";

	return 0;
}