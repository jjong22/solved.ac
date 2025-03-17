#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	int music[8];

	int upward = 0;
	int downward = 0;

	for (int i = 0; i < 8; i++)
	{
		cin >> music[i];
	}

	if (music[0] == 1)
	{
		for (int i = 0; i < 7; i++)
		{
			if (music[i] + 1 == music[i + 1])
			{
				upward += 1;
			}
		}
		if (upward == 7)
		{
			cout << "ascending";
		}
		else
		{
			cout << "mixed";
		}
	}
	
	else if (music[0] == 8)
	{
		for (int i = 0; i < 7; i++)
		{
			if (music[i] - 1 == music[i + 1])
			{
				downward += 1;
			}
		}
		if (downward == 7)
		{
			cout << "descending";
		}
		else
		{
			cout << "mixed";
		}
	}

	else
	{
		cout << "mixed";
	}
}