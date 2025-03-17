#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;
int main()
{
	int n;
	cin >> n;

	int count = 0;
	int number = 600;
	bool is_ok = 0;
	vector<int> v1;

	while (true)
	{
		for (int i = 0; i < to_string(number).length() - 2; i++)
		{
			if (to_string(number)[i] == '6'
				and to_string(number)[i+1] == '6'
				and to_string(number)[i+2] == '6')
			{
				is_ok = 1;
				break;
			}
		}

		if (is_ok == 1)
		{
			count += 1;
		}

		if (count == n)
		{
			break;
		}
		
		number += 1;
		is_ok = 0;
	}

	cout << number;
}