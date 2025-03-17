#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
	vector<int> fibonachi;
	fibonachi.push_back(0);
	fibonachi.push_back(1);

	int n;
	cin >> n;
	for (int i = 2; i <= n; i++)
	{
		fibonachi.push_back(fibonachi[i - 2] + fibonachi[i - 1]);
	}

	cout << fibonachi[n];
}