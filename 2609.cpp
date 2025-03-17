#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;
int main()
{
	int a, b;
	int a_mod = 1;
	int b_mod = 1;

	cin >> a >> b;

	int max, min;

	for (int i = 1; i < 10000; i++)
	{
		if (a % i == 0 and b % i == 0)
		{
			min = i;
		}
	}
	
	a_mod = a / min;
	b_mod = b / min;

	max = min * (a_mod * b_mod);

	cout << min << '\n' << max;

}