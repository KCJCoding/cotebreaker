#include <string>
#include <vector>

int solution(int n, std::vector<int> lost, std::vector<int> reserve)
{
	std::vector<int> student(n, 1);
	int answer = 0;

	for (int i : reserve)
		student[i - 1] += 1; //여분 체육복을 가지고 있는 학생
	for (int i : lost)
		student[i - 1] -= 1; //체육복을 도둑맞은 학생

	for (int i = 0; i < n; i++)
	{
		if (student[i] == 0) //현재 체육복이 없는 번호라면
		{
			//앞에서 빌려오기
			if (i - 1 >= 0 && student[i - 1] == 2) //앞의 위치가 0보다 크고 체육복이 있다면
			{
				student[i]++;
				student[i - 1]--;
			}
			//혹은 뒤에서 빌려오기
			else if (i + 1 <= n - 1 && student[i + 1] == 2) //뒤의 위치가 끝 이전이고 체육복이 있다면
			{
				student[i]++;
				student[i + 1]--;
			}
		}
	}
	for (int i : student)
	{
		if (i != 0) // 0이 아님 -> 1이거나 2 (체육복이 있거나 남음)
			answer++;
	}
	return answer;
}

#include <iostream>

int main() //예제 main
{
	std::vector<int> lost;
	std::vector<int> reserve;
	lost.push_back(2);
	lost.push_back(4);

	reserve.push_back(1);
	reserve.push_back(3);
	reserve.push_back(5);
	std::cout << solution(5, lost, reserve);
	return 0;
}
