#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;
int main()
{
	string word;

	cin >> word;

	int save[26] = 
	{-1,-1,-1,-1,-1,
	-1,-1,-1,-1,-1 ,
	-1,-1,-1,-1,-1 ,
	-1,-1,-1,-1,-1 ,
	-1,-1,-1,-1,-1 ,
	-1};

	int length = word.length();

	for (int i = 0; i < 26; i++)
	{
		for (int j = 0; j < length; j++)
		{
			if (int(word[j]) == i + 97 and save[i] == -1)
			{
				save[i] += j+1;
			}
		}
	}

	for (int i = 0; i < 26; i++)
	{
		cout << save[i];
		if (i != 25)
		{
			cout << " ";
		}
	}
}