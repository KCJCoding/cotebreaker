#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(0);
	cin.tie(0);

    int t, n, d, i = 1;
	cin >> t;
	while(t--)
	{        
		cin >> n >> d;
		cout << "#" << i++ << " " << ceil((double)n / (2 * d + 1)) << "\n";
	}    
	return 0;
}
