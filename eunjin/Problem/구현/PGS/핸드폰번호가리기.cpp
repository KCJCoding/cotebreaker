#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
	string star;
	for (int i = 0; i < phone_number.length() - 4; i++)
		star.append("*");
	phone_number.replace(0, phone_number.length() - 4, star);
    return phone_number;
}

#include <iostream>

int main() //test main
{
	cout << solution("01012345678");

	return 0;
}