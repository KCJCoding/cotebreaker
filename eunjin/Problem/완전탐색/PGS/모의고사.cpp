#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
	vector<int> cnt(3);
	
	int student_1 [5] = {1, 2, 3, 4, 5};
	int student_2 [8] = {2, 1, 2, 3, 2, 4, 2, 5};
	int student_3 [10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
	
	for (int i = 0; i < answers.size(); i++)
	{
		if (answers[i] == student_1[i % 5])
			cnt[0]++;
		if (answers[i] == student_2[i % 8])
			cnt[1]++;
		if (answers[i] == student_3[i % 10]) // 각자 다른 답을 작성했을 수도 있기 때문에 (같은 답을 했을 수도 있어서) if문으로 작성해야 한다
			cnt[2]++;
	}

	int max_score = *max_element(cnt.begin(), cnt.end());

	for (int i = 0; i < 3; i++)
	{
		if (cnt[i] == max_score)
			answer.push_back(i + 1);
	}
    return answer;
}
