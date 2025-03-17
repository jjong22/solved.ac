#include <iostream>
#include <string>

using namespace std;

int main()
{
	string name;
	cin >> name;
	for (int i = 0; i < name.size() / 10; i++)
	{
		cout << name.substr(i * 10,10) << '\n';
	}
	cout << name.substr( (name.size() / 10) * 10, name.size() % 10 );
}