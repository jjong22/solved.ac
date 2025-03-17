#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;
int main()
{
	string word;
	vector<int> v1, v2;

	cin >> word;

	for (int i = 0; i < word.length(); i++)
	{
		v1.push_back(word[i]);

		if (v1[i] >= 65 and v1[i] <= 90)
		{
			v2.push_back(v1[i] + 32);
		}
		else
		{
			v2.push_back(v1[i] - 32);
		}

		printf("%s", &v2[i]);
	}
}