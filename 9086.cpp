#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int n;
	string name;
	string save;
	vector<string> str1;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> name;
		str1.push_back(name);
	}

	for (int i = 0; i < n; i++)
	{
		int length = str1[i].length();
		cout << str1[i][0] << str1[i][length -1] << '\n';
	}
}