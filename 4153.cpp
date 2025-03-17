#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int a, b, c;
	int count = 0;

	vector<int> v1;

	do
	{
		cin >> a >> b >> c;

		if (a * a == b * b + c * c)
		{
			v1.push_back(1);
			count += 1;
		}
		else if (b * b == a * a + c * c)
		{
			v1.push_back(1);
			count += 1;
		}
		else if (c * c == a * a + b * b)
		{
			v1.push_back(1);
			count += 1;
		}
		else
		{
			v1.push_back(0);
			count += 1;
		}
	} while ((a + b + c) != 0);

	for (int i = 0; i < count -1; i++)
	{
		if (v1[i] == 1)
		{
			cout << "right" << '\n';
		}
		else
		{
			cout << "wrong" << '\n';
		}
	}
}