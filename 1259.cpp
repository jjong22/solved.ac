#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;
int main()
{
	int n = 1;
	int save;

	int count = 0;

	vector<int> v1, v2;

	while (n != 0)
	{
		cin >> n;
		save = n;

		if (n == 0)
		{
			break;
		}

		int length = to_string(save).length();
		
		for (int i = 0; i < length; i++)
		{
			v1.push_back(save % 10);

			save = save / 10;
		}

		for (int i = 0; i < (length + 1) / 2; i++)
		{
			if (v1[i] != v1[length -1 -i])
			{
				count = 1;
				break;
			}
		}

		if (count == 0)
		{
			v2.push_back(1);
		}
		else
		{
			v2.push_back(0);
		}

		for (int i = 0; i < length; i++)
		{
			v1.erase(v1.begin());
		}

		count = 0;
	}

	for (int i = 0; i < size(v2); i++)
	{
		if (v2[i] == 1)
		{
			cout << "yes" << '\n';
		}
		else
		{
			cout << "no" << '\n';
		}
	}
}