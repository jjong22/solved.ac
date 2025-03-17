#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;
int main()
{
	int a, b, c;
	cin >> a;
	cin >> b;
	cin >> c;

	vector<int> v1;

	string abc = to_string(a*b*c);

	int length = abc.length();

	for (int i = 0; i < length; i++)
	{
		v1.push_back(abc[i]);
	}

	int save[10] =
	{ 0,0,0,0,0,
	0,0,0,0,0 };

	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < length; j++)
		{
			if (int(v1[j]) == i + 48)
			{
				save[i] = save[i] + 1;
			}
		}
	}

	for (int i = 0; i < 10; i++)
	{
		cout << save[i] << '\n';
	}
}