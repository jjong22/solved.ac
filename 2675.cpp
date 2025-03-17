#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	int test;
	cin >> test;

	int rec, length;
	string text;
	string str[1000];

	for (int i = 0; i < test; i++)
	{
		cin >> rec >> text;
		length = text.length();
		for (int j = 0; j < length; j++)
		{
			for (int k = 0; k < rec; k++)
			{
				str[i] = str[i] + text[j];
			}
		}
	}

	for (int l = 0; l < test; l++)
	{
		cout << str[l] << '\n';
	}
}