#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	int a, b, v;

	int day = 1;
	int save;

	cin >> a >> b >> v;

	day = (v - a) / (a - b) + 2;

	if ((v - a) % (a - b) == 0)
	{
		day = (v - a) / (a - b) + 1;
	}


	cout << day;
}